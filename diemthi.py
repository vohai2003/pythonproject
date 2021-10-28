import scrapy


class DiemthiSpider(scrapy.Spider):
    name = 'diemthi'
    allowed_domains = ['https://vietnamnet.vn/vn/giao-duc/tra-cuu-diem-thi-thpt/']
    start_urls = ['http://https://vietnamnet.vn/vn/giao-duc/tra-cuu-diem-thi-thpt//']

    def parse(self, response):
        pass
