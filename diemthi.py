import scrapy
import logging
from bs4 import BeautifulSoup as bs
logging.getLogger('scrapy').setLevel(logging.WARNING)

class DiemthiSpider(scrapy.Spider):
    '''start_urls = []
    for i in range (1,1000000):
        start_urls.append("https://www.vietnamnet.vn/vn/giao-duc/tra-cuu-diem-thi-thpt/?y=2021&sbd=33"+"{:06}".format(i))'''
    start_urls = ["https://www.vietnamnet.vn/vn/giao-duc/tra-cuu-diem-thi-thpt/?y=2021&sbd=33000001"]
    name = 'diemthi'
    def parse(self, response):
        if(response.xpath('/html/body/div[1]/div[2]/div[3]/h5[1]').getall()) ==[]:
            for i in range (2,8):
                rep = response.xpath('/html/body/div[1]/div[2]/div[3]/div[{:d}]'.format(i)).get()
                rep = rep.replace('<div class="d-flex justify-content-between search-result-line py-3 px-3">','')
                rep = rep.replace('<div class="font-weight-bold">','')
                rep = rep.replace('<span>','')
                rep = rep.replace('</span>','')
                rep = rep.replace('</div></div>',',')
                rep = rep.replace('</div>','":')
                rep = rep.replace('<div>','"')
                rep.join(rep.split('\n'))
                print(rep)
