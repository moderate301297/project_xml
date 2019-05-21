# -*- coding: utf-8 -*-

import scrapy
import urllib
# from job_travel.items import AmazonItem
import os

class KHVietSpider(scrapy.Spider):
    name = "khviet"

    def __init__(self):
		self.ids_seen = set()
        
    def start_requests(self):
        urls = [
            'https://dulichkhatvongviet.com/du-lich-trong-nuoc/',
            'https://dulichkhatvongviet.com/du-lich-nuoc-ngoai/'
        ]
        for i in range(1, 31):
            yield scrapy.Request(
                url=urls[0]+"page/"+str(i),
                callback=self.parse_page
            )
        for i in range(1, 15):
            yield scrapy.Request(
                url=urls[1]+"page/"+str(i),
                callback=self.parse_page
            )
    def parse_page(self, response):
        list_next_url1 = response.css('div.post-content h3 a::attr(href)').extract()
        print(len(list_next_url1))
        for url in list_next_url1:
                yield scrapy.Request(
                    # url = url,
                    url=self.checkUrl(url),
                    callback=self.parse
                )
    
    def parse(self, response):

        name_tour = response.css('h1.entry-title a::text').extract_first()
        url_tour = response.request.url
        type_tour = response.css('div.breadcrumbs a:nth-child(4)::text').extract_first()
        number_date = response.xpath('//div[@class="entry entry-content"]/p[1]/text()[3]').extract_first()
        start_date = response.xpath('//div[@class="entry entry-content"]/p[1]/text()[9]').extract_first()
        cost_tour = response.xpath('//div[@class="entry entry-content"]/p[1]/text()[5]').extract_first()
        # print(url_tour)
        # number_date_new = self.checkNumberDate(number_date[i])
        url_new = self.checkUrl(url_tour)
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
            'source': 'khviet',
            'title': name_tour.encode('utf-8'),
            'type_tour': type_tour.encode('utf-8'),
            'url_tour': url_new.encode('utf-8'),
            'number_date': number_date_new,
            'begin_date': start_date_new,
            'cost_tour': cost_tour_new
        }

    def checkUrl(self, url):
        if "http" in url:
            return url
        else:
            return "https://dulichkhatvongviet.com/"+url

    def checkNumberDate(self, number_date):
        return (number_date[7])