from _ast import List

import scrapy
from scrapy import Selector, Request


class RwidSpider(scrapy.Spider):
    name = 'rwid'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost:5000/']

    def __init__(self, name=None, **kwargs):
        super().__init__(name=None, **kwargs)

    def parse(self, response):
        # pass
        # yield {"title":response.css("title::text").get()}
        data = {
            "username": "admin",
            "password": "admin12345",
        }

        return scrapy.FormRequest.from_response(
            response,
            url="http://localhost:5000/login",
            formdata=data,
            callback=self.after_login
        )

    def after_login(self, response):
        yield Request(url=self.start_urls[0], callback=self.action)
        # pass
        # scrapy.utils.response.open_in_browser(response)

    def action(self, response):
        detail_products: List[Selector] = response.css(".card-title a")
        for detail in detail_products:
            href = detail.attrib.get("href")
            yield response.follow(href, callback=self.parse_detail)


        paginations: List[Selector] = response.css(".pagination a.page-link")
        for pagination in paginations:
            href = pagination.attrib.get("href")
            yield response.follow(href, callback=self.action)


    def parse_detail(self, response):
        # yield {"title": response.css("title::text").get()}
        image = response.css(".card-img-top").attrib.get("src")

        title = response.css(".card-title::text").get()
        stock = response.css(".card-stock::text").get()
        price = response.css(".card-price::text").get()
        description = response.css(".card-text::text").get()

        return {
            "image": image,
            "title": title,
            "stock": stock,
            "price": price,
            "description": description
        }