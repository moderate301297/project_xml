# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MainItem(scrapy.Item):
    source = scrapy.Field()
    name_tour = scrapy.Field()
    type_tour = scrapy.Field()
    url_tour = scrapy.Field()
    cost_tour = scrapy.Field()
    number_date = scrapy.Field()
    start_date = scrapy.Field()

