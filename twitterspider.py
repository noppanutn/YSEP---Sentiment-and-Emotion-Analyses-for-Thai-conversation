#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:53:26 2018

@author: nopchamnan.n.aa
"""

import scrapy

class TwitterSpider(scrapy.Spider):
    name = 'twitter_spider'
    start_urls = ['https://twitter.com']