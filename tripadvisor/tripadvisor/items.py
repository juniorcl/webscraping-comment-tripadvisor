# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TripadvisorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #fields
    author_comment = scrapy.Field()
    author_address = scrapy.Field()
    comment_title = scrapy.Field()
    comment_body = scrapy.Field()
    comment_data = scrapy.Field()