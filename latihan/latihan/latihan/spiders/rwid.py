import scrapy


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
            callback=self.after_login,
        )

    def after_login(self, response):
        # print(response.body)
        yield {"title": response.css("title::text").get()}
        # pass
