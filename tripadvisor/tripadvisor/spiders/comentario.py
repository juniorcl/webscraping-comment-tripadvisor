# -*- coding: utf-8 -*-
import scrapy
from ..items import TripadvisorItem #importa a classe de dentro do items.py

class ComentarioSpider(scrapy.Spider):
    name = 'comentario' #nome da aranha que estou utilziando
    allowed_domains = ['tripadvisor.com.br'] #os domínios do site
    start_urls = ['https://www.tripadvisor.com.br/Attraction_Review-g303441-d553398-Reviews-Parque_Barigui-Curitiba_State_of_Parana.html#REVIEWS'] #link da página onde pegaremos os comentários

    def parse(self, response):
        item = TripadvisorItem() #chama o TripadvisorItem definido no comentario.py
        quadros_de_comentarios = response.xpath("//div[@class='location-review-card-Card__ui_card--2Mri0 location-review-card-Card__card--o3LVm location-review-card-Card__section--NiAcw']") #selciona todos os quadros de comentarios.
        
        #Passa por cada comentário (quadro) definido dentro dos quadros de comentários
        #definido anteriormente.
        for quadro in quadros_de_comentarios:
            item['autor_comentario'] = quadro.xpath(".//div[@class='social-member-event-MemberEventOnObjectBlock__event_type--3njyv']/span/a/text()").get() #seleciona o autor de cada quadro
            item['autor_endereco'] = quadro.xpath(".//span[@class='default social-member-common-MemberHometown__hometown--3kM9S small']/text()").get() #o endereço da pessoa na página
            item['comentario_titulo'] = quadro.xpath(".//div[@class='location-review-review-list-parts-ReviewTitle__reviewTitle--2GO9Z']/a//span/text()").get() #o título do comentario
            item['comentario_corpo'] = quadro.xpath(".//div[@class='cPQsENeY']/q/span/text()").get() #o corpo do comentario
            item['comentario_data'] = quadro.xpath(".//span[@class='location-review-review-list-parts-EventDate__event_date--1epHa']/text()").get() #retira a data da experiência
            yield item

        #Abaixo é adicionado o link para prosseguir para a próxima página. E se for verdade, então
        #entra no if para seguir para a próxima página e chama o método parse da classe novamente.
        next_page = response.xpath("//a[@class='ui_button nav next primary ' and text()='Próximas']/@href")
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)