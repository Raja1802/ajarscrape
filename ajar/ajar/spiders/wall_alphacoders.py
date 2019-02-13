#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AjarWallAlphaItem


class QuotesSpider(CrawlSpider):

    name = 'wallalpha'
    allowed_domains = ['wall.alphacoders.com']
    start_urls = ['https://wall.alphacoders.com/']

    rules = (Rule(sle(allow='big.php'), callback='parse_images',
             follow=True), )

    def parse_images(self, response):
        image = []
        image = AjarWallAlphaItem()

        image['image_url'] = \
            response.css('#page_container > div.center.img-container-desktop > a::attr(href)'
                         ).get()
        image['image_tags'] = \
            response.css('#list_tags > div.tag-element > a::text'
                         ).getall()
        image['image_type'] = \
            response.css('#page_container > div.center > h2 > a::attr(title)'
                         ).get()

        return image
