import random
import scrapy
import requests #请求网页数据
from bs4 import BeautifulSoup #美味汤解析数据
import pandas as pd
import time
from tqdm import trange #获取爬取速度



class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ["bilibili.com"]
    start_urls = ("https://api.bilibili.com/x/v2/dm/history?type=1&oid=141367679&date=2020-09-24",)

    def start_requests(self):
        urls = []
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # file = open("bilibili_danmu.txt", 'w')
        # soup = BeautifulSoup(response.text,features="lxml")
        # data = soup.find_all("d")
        # danmu = [data[i].text for i in range(len(data))]
        # for items in danmu:
        #     file.write(items)
        #     file.write("\n")
        # time.sleep(3)
        # file.close()
        filename = "bilibili_danmu.txt"
        open(filename, 'w').write(str(response.body, encoding="utf8"))



