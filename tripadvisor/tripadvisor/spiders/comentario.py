# -*- coding: utf-8 -*-
import scrapy


class ComentarioSpider(scrapy.Spider):
    name = 'comentario'
    allowed_domains = ['tripadvisor.com.br']
    start_urls = ['http://tripadvisor.com.br/']

    def parse(self, response):
        pass
