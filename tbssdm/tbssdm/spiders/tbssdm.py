import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.http import FormRequest

class TbssdmSpider(scrapy.Spider):
    name = "tbssdm"
    # allowed_domains = ["sdm.titianbangunsarana.co.id"]
    start_urls = ["https://sdm.titianbangunsarana.co.id/index.php/Auth/login"]

    def parse(self, response):
        return FormRequest.from_response(response, formdata={
            'identity': '',
            'password': '',
            # 'submit': 'Login'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        next_url = "https://sdm.titianbangunsarana.co.id/index.php/Sdm_pegawai/index"
        yield response.follow(next_url, callback=self.get_karyawan)

    def get_karyawan(self, response):
        # table = response.xpath('//table[@id="mytable"]//tbody')
        # rows = table.xpath('//tr')

        for row in response.xpath('//table[@id="mytable"]//tbody//tr'):
            yield {
                'nik': row.xpath('td[2]//text()').extract_first()
            }


        # open_in_browser(response)