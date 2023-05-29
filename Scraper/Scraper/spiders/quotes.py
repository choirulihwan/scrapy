import sys

import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
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

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        else:
            pass
