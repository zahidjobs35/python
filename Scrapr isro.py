# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:50:55 2022

@author: Zahid
"""

import scrapy
import requests
from scrapy.http import TextResponse
# from Gov import items

class ISROSpider(scrapy.Spider):
    name = "isro"

    def start_requests(self):

        self.base_url = 'https://www.isro.gov.in/careers?&&field_isro_centre_value=All'

        yield scrapy.Request(url=self.base_url, callback=self.parse)

    def parse(self, response):
        data = items.ISROSpider()

        pages = response.xpath('//*[@class="pager-last last"]/a/@href').extract_first()[-1]
        for var in range(int(pages)):
            response = requests.request("GET", url=self.base_url, params={'page':var})
            response = scrapy.http.TextResponse(url=self.base_url+'&page='+str(var), body=response.content)
            trs = response.xpath('//*[@class="view-content"]/table/tbody/tr')   
        
            for i in trs:
                data['Location'] = i.xpath('td[1]/text()').extract_first().strip()
                data['Post'] = 'https://www.isro.gov.in' + i.xpath('td[2]/a/@href').extract_first()
                data['Advertisement_Number'] = i.xpath('td[3]/text()').extract_first().strip()

                yield data
                
                
                print(data)