# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    ranking = scrapy.Field()
    quote = scrapy.Field()
    status = scrapy.Field()
    description = scrapy.Field()
    href = scrapy.Field()
    pass

