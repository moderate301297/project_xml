# -*- coding: utf-8 -*-

import scrapy
import urllib
# from job_travel.items import AmazonItem
import os

list_url = []

class VietTSpider(scrapy.Spider):
    name = "vietT"

    def __init__(self):
		self.ids_seen = set()
        
    def start_requests(self):
            
		yield scrapy.Request(
            url="https://vietrantour.com.vn/tour-trong-nuoc.html",
            callback=self.parse_page
        )
    def parse_page(self, response):
        list_next_url1 = response.css('li a::attr(href)').extract()
        print(len(list_next_url1))
        for url in list_next_url1:
                yield scrapy.Request(
                    url=self.checkUrl(url),
                    callback=self.parse_page_next
                )
    def parse_page_next(self, response):

        list_url_tour = response.css('div.box-row a::attr(href)').extract()
        
        for url in list_url_tour:
            yield scrapy.Request(
                url=self.checkUrl(url),
                callback=self.parse
            )
            
    def parse(self, response):

        name_tour = response.css('h1.title::text').extract_first()
        type_tour = response.css('div.navi-cate a:nth-child(2)::text').extract_first()
        url_tour = response.request.url
        number_date = response.css('div.infor.col-md-12 span:nth-child(3)::text').extract_first()
        start_date = response.css('div.infor.col-md-12 span:nth-child(5) span::text').extract_first()
        cost_tour = response.css('div.dtpricen span::text').extract_first()
        # print(url_tour)
        url_new = self.checkUrl(url_tour)
            # number_date_new = self.checkNumberDate(number_date[i])
        if number_date is not None:
            number_date_new = number_date.encode('utf-8')
        else:
            number_date_new = number_date

        if start_date is not None:
            start_date_new = start_date.encode('utf-8')
        else:
            start_date_new = start_date

        if cost_tour is not None:
            cost_tour_new = cost_tour.encode('utf-8')
        else:
            cost_tour_new = cost_tour

        yield{
            'source': 'vietT',
            'name_tour': name_tour.encode('utf-8'),
            'type_tour': type_tour.encode('utf-8'),
            'link': url_new.encode('utf-8'),
            'number_date': number_date_new,
            'start_date': start_date_new,
            'cost_tour': cost_tour_new
        }

    def checkUrl(self, url):
        if "http" in url:
            return url
        else:
            return "https://vietrantour.com.vn"+url

    def checkNumberDate(self, number_date):
        return (number_date[7])