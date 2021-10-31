import scrapy
import logging
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
wb = Workbook()
dest_filename = 'C:/Users/vohai2003/Pythonproject/crawled_data.xlsx'
ws = wb.active
ws.title = "Crawled_data"
ws.append(["SBD","Toán","Văn","Lý","Hóa","Sinh","Sử","Địa","Ngoại ngữ","GDCD"])
j = 0
class DiemthiSpider(scrapy.Spider):
    start_urls = []
    for i in range (1,22001):
        start_urls.append("https://www.vietnamnet.vn/vn/giao-duc/tra-cuu-diem-thi-thpt/?y=2021&sbd=33"+"{:06}".format(i))
    name = 'diemthi'
    def parse(self, response):
        global j
        j += 1
        temp = ["33"+"{:06}".format(j),"x","x","x","x","x","x","x","x","x"]
        if(response.xpath('/html/body/div[1]/div[2]/div[3]/h5[1]').getall()) ==[]:
            rep = response.xpath('//div[@class="d-flex justify-content-between search-result-line py-3 px-3"]')
            for repline in rep:
                data = repline.xpath('.//text()').getall()
                if data[0].find("Ngoại ngữ") != -1:
                    temp[8] = float(data[3])
                else:
                    if data[0] == "Toán":
                        temp[1] = float(data[1])
                    elif data[0] == "Văn":
                        temp[2] = float(data[1])
                    elif data[0] == "Lý":
                        temp[3] = float(data[1])
                    elif data[0] == "Hóa":
                        temp[4] = float(data[1])
                    elif data[0] == "Sinh":
                        temp[5] = float(data[1])
                    elif data[0] == "Sử":
                        temp[6] = float(data[1])
                    elif data[0] == "Địa":
                        temp[7] = float(data[1])
                    elif data[0] == "GDCD":
                        temp[9] = float(data[1])
            ws.append(temp)
        if j%100 ==0:
            wb.save(filename = dest_filename)
