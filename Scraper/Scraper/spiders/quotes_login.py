import sys

import scrapy
from scrapy.http import FormRequest
# from scrapy.utils.response import open_in_browser

class QuoteSpider(scrapy.Spider):
    name = "quotes_login"
    start_urls = [
        "https://quotes.toscrape.com/login"
    ]

    def parse(self, response):
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'a',
            'password': 'a'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        # open_in_browser(response)
        quotes = response.css("div.quote")

        for quote in quotes:
            content = quote.css(".text::text").get()
            author = quote.css(".author::text").get()
            tag = quote.css(".tag::text").getall()

            yield {
                'content': content,
                'author': author,
                'tag': tag
            }