# -*- coding: utf-8 -*-

import scrapy
import urllib
# from job_travel.items import AmazonItem
from scrapy_splash import SplashRequest
import os

fun ="""
function main(splash, args)
    local num_scrolls = 10
    local scroll_delay = 1.0

    local scroll_to = splash:jsfunc('window.scrollTo')
    local get_body_height = splash:jsfunc(
        'function() {return document.body.scrollHeight;}'
    )
    assert(splash:go(splash.args.url))
    assert(splash:wait(0.5))

    for _ = 1, num_scrolls do
        scroll_to(0, get_body_height())
        splash:wait(scroll_delay)
    end        
    return splash:html()
end
"""
list_url = []

class TravelSpider(scrapy.Spider):
    name = "travel"

    def __init__(self):
		self.ids_seen = set()
        
    def start_requests(self):

		yield scrapy.Request(
            url="https://travel.com.vn",
            callback=self.parse_page
        )
    def parse_page(self, response):
        list_next_url = response.css('div.row.content a::attr(href)').extract()
        for i in range(0,len(list_next_url)):
            if (list_next_url[i] in list_url) or ("/du-lich" not in list_next_url[i]):
                continue
            else:
                list_url.append(list_next_url[i])
        # print(len(list_url))
        for url in list_url:
            yield SplashRequest(
                url=self.checkUrl(url),
                # url="https://travel.com.vn/du-lich-ha-noi.aspx",
                callback=self.parse,
                endpoint='execute',
                args={
                    'lua_source': fun      }
            )
            
    def parse(self, response):

        name_tour = response.css('div.tour-name a::text').extract()
        type_tour = response.css('#breadcrumb div div span:nth-child(2) a span::text').extract_first(),
        url_tour = response.css('div.tour-name a::attr(href)').extract()
        number_date = response.css('div.row.mg-listtour div:nth-child(3)::text').extract()
        start_date = response.css('div.row.mg-listtour div:nth-child(2)::text').extract()
        cost_tour = response.css('div.price-new::text').extract()
        listlength = len(name_tour)
        for i in range(0,listlength):
            url_new = self.checkUrl(url_tour[i])

            # number_date_new = self.checkNumberDate(number_date[i])
            yield{
                'name_tour': name_tour[i].encode('utf-8'),
                'type_tour': type_tour[0].encode('utf-8'),
                'url_tour': url_new.encode('utf-8'),
                'number_date': number_date[i].encode('utf-8'),
                'start_date': start_date[i].encode('utf-8'),
                'cost_tour': cost_tour[i].encode('utf-8')
            }
        print(listlength)

    def checkUrl(self, url):
        if "http" in url:
            return url
        else:
            return "https://travel.com.vn"+url

    def checkNumberDate(self, number_date):
        return (number_date[7])