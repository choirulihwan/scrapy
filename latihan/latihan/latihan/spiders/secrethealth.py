from typing import List

import scrapy
from cssselect import Selector



class SecrethealthSpider(scrapy.Spider):
    name = 'secrethealth'
    allowed_domains = ['secrethealth.net']
    start_urls = ['https://www.secrethealth.net/']

    # allowed_domains = ['detik.com']
    # start_urls = ['https://sport.detik.com/sepakbola/']

    # allowed_domains = ['detik.com']
    # start_urls = ['https://sport.detik.com/sepakbola/']

    #allowed_domains = ['167.71.212.167']
    #start_urls = ['http://167.71.212.167/engine_affiliate/']

    def parse(self, response):
        #
        most_commented: List[Selector] = response.css('h2.entry-title a')

        for detail in most_commented:
            href = detail.attrib.get('href')
            yield response.follow(href, callback=self.parse_detail)

        # yield {"title": response.css("title::text").get()}
        # yield {"title": response.xpath('//title/text()').extract()}
        # pass
        # data = {
        #     "identity":"1071019",
        #     "password":"philos03*",
        #     "submit":"Login"
        # }
        # return scrapy.FormRequest(
        #     url='https://www.drugvisions.com/tbs_sdm/index.php/Auth/login',
        #     formdata=data,
        #     callback=self.after_login
        # )

    def after_login(self, response):
        # list_menu: List[Selector] = response.css('#main_menu ul li b a')
        # for detail in list_menu:
        #     href = detail.attrib.get('href')
        #     yield response.follow(href, callback=self.parse_detail)
        yield {"title": response.css("title::text").get()}

    def parse_detail(self, response):
        # yield {"title": response.css("title::text").get()}
        title = response.css('h1.entry-title::text').get()
        author = response.css('span.posted-author a::text').get()

        return {
            "title":title,
            "author":author
        }
