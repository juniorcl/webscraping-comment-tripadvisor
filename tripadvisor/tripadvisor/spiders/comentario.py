# -*- coding: utf-8 -*-
import scrapy
from ..items import TripadvisorItem

class ComentarioSpider(scrapy.Spider):
    name = 'comentario'
    allowed_domains = ['tripadvisor.com.br']
    start_urls = ['http://tripadvisor.com.br/']

    def parse(self, response):
        item = TripadvisorItem()
        quadros_de_comentarios = response.xpath("//div[@class='location-review-card-Card__ui_card--2Mri0 location-review-card-Card__card--o3LVm location-review-card-Card__section--NiAcw']") #selciona os quadros
        
        for quadro in quadros_de_comentarios:
            item['autor_comentario'] = quadro.xpath(".//div[@class='social-member-event-MemberEventOnObjectBlock__event_type--3njyv']/span/a/text()").get() #seleciona o autor de cada quadro
            item['autor_endereco'] = quadro.xpath("") #o endereço da pessoa na página
            item['comentario_titulo'] = quadro.xpath("") #o título do comentario
            item['comentario_corpo'] = quadro.xpath("") #o corpo do comentario
            item['comentario_data'] = quadro.xpath("") #retira a data da experiência
            yield item