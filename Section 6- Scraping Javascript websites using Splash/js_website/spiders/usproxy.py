# -*- coding: utf-8 -*-
import scrapy


class UsproxySpider(scrapy.Spider):
    name = 'usproxy'
    allowed_domains= ['us-proxy.org']
    start_urls= ['http://us-proxy.org']

    

    def parse(self, response):
        pass