# -*- coding: utf-8 -*-
import scrapy
from ..items import TripadvisorItem #import the class inside the item.py

class ComentarioSpider(scrapy.Spider):
    name = 'comentario' #the name of the spider
    allowed_domains = ['tripadvisor.com.br'] #the site domain
    start_urls = ['https://www.tripadvisor.com.br/Attraction_Review-g303441-d553398-Reviews-Parque_Barigui-Curitiba_State_of_Parana.html#REVIEWS'] #link of the page where the comments will be taken.

    def parse(self, response):
        item = TripadvisorItem() #It calls the TripadvisorItem defined into comentario.py
        comment_frames = response.xpath("//div[@class='location-review-card-Card__ui_card--2Mri0 location-review-card-Card__card--o3LVm location-review-card-Card__section--NiAcw']") #It selects all the commentaries boxes.
        
        #this goes through each comment (frames) defined within the comment frames defined previously.
        for frame in comment_frames:
            item['author_comment'] = frame.xpath(".//div[@class='social-member-event-MemberEventOnObjectBlock__event_type--3njyv']/span/a/text()").get()
            item['author_address'] = frame.xpath(".//span[@class='default social-member-common-MemberHometown__hometown--3kM9S small']/text()").get()
            item['comment_title'] = frame.xpath(".//div[@class='location-review-review-list-parts-ReviewTitle__reviewTitle--2GO9Z']/a//span/text()").get()
            item['comment_body'] = frame.xpath(".//div[@class='cPQsENeY']/q/span/text()").get()
            item['comment_data'] = frame.xpath(".//span[@class='location-review-review-list-parts-EventDate__event_date--1epHa']/text()").get()
            yield item

        #Below is added the link to proceed to the next page. And if that's true, then enter the 'if' to proceed to the next page and call the class's parse method again.
        next_page = response.xpath("//a[@class='ui_button nav next primary ' and text()='Próximas']/@href").get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)