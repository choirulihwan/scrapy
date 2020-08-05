from typing import List

import scrapy
from cssselect import Selector



class SecrethealthSpider(scrapy.Spider):
    name = 'olx'
    allowed_domains = ['olx.co.id']
    start_urls = ['https://www.olx.co.id/yogyakarta-di_g2000032/mobil-bekas_c198/q-mobil-bekas']

    def parse(self, response):
        cars: List[Selector] = response.css('li.EIR5N a')
        for detail in cars:
            href = detail.attrib.get('href')
            yield response.follow(href, callback=self.parse_detail)

        paginations: List[Selector] = response.css('')

    def parse_detail(self, response):
        # yield {"title": response.css("title::text").get()}
        title = response.css('h1._3rJ6e::text').get()
        price = response.css('section._2wMiF span._2xKfz::text').get()
        #
        return {
            "title":title,
            "price":price
        }
