import scrapy


class RwidSpider(scrapy.Spider):
    name = 'rwid'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost:5000/']

    def parse(self, response):
        pass
