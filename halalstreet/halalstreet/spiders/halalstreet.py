import scrapy
from ..items import HalalstreetItem


class HalalstreetSpider(scrapy.Spider):
    name = "halalstreet"
    # page_number = 1
    # allowed_domains = ["halalstreet.co.uk"]
    start_urls = ["https://www.halalstreet.co.uk/product-category/malaysian-products-uk/"]

    def parse(self, response):
        products = response.css("div.content-product")

        for product in products:
            items = HalalstreetItem()
            product_name = product.css("div.text-center.product-details h2.product-title a::text").get()
            product_price = product.css("div.text-center.product-details span.price span.woocommerce-Price-amount.amount bdi::text").get()

            items['product_name'] = product_name
            items['product_price'] = product_price

            yield items

        link_next_page = response.css('a.page-numbers::attr(href)').get()
        next_page = response.css('a.page-numbers::text').get()
        curr_page = response.css('span.page-numbers.current::text').get()
        if next_page > curr_page:
            yield response.follow(link_next_page, callback=self.parse)
        else:
            pass

        # if self.page_number < 2:
        #     self.page_number += 1
        #     next_page = self.start_urls[0] + str(self.page_number) + "/"
        #     yield response.follow(next_page, callback=self.parse)

