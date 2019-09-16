# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InternshalaItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    start_date = scrapy.Field()
    duration = scrapy.Field()
    link = scrapy.Field()
