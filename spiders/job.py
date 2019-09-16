# -*- coding: utf-8 -*-
import scrapy
from ..items import InternshalaItem


class JobSpider(scrapy.Spider):
    name = 'job'
    start_urls = ['https://internshala.com/internships']

    def parse(self, response):
        iteams=InternshalaItem()
        all_div_tags = response.css(".internship_meta")
        #print(all_div_tags)
        link=response.css("a.view_detail_button::attr(href)").extract()
        i=0
        for quote in all_div_tags[1:]:
            title=quote.css("h4").css("a::text").get()
            company=quote.css("h4").css(".link_display_like_text::attr(title)").get()
            location=quote.css("span").css(".location_link::text").get()
            start_date=quote.css("td").css("div#start-date-first::text").get()
            duration=quote.css("div.table-responsive").css("td::text").extract()
            i=i+1

            #print("DURATION",duration[2].strip())
            iteams["title"]=title
            #print("COMPANY",company)
            iteams["company"]=company
            iteams["location"]=location
            iteams["start_date"]=start_date
            iteams["duration"]=duration[2].strip()
            iteams["link"]="https://internshala.com"+link[i]
            yield iteams
        next_page=response.css("nav").css("a#navigation-forward::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
