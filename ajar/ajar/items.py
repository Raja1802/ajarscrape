# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 9naime anime info downloader


class AjarItem(scrapy.Item):
        name = scrapy.Field()
        image = scrapy.Field()
        synonyms = scrapy.Field()
        types = scrapy.Field()
        studios = scrapy.Field()
        aired = scrapy.Field()
        status = scrapy.Field()
        scores = scrapy.Field()
        premired = scrapy.Field()
        durination = scrapy.Field()
        quality = scrapy.Field()
        gener = scrapy.Field()
        about = scrapy.Field()
        tags = scrapy.Field()
        cover = scrapy.Field()

# pixabay images links grabber


class AjarPixabayItem(scrapy.Item):
        img_srcset = scrapy.Field()
        img_src = scrapy.Field()
        img_tags = scrapy.Field()
# gogo anime urls collector


class AjarGogoanimeItem(scrapy.Item):
        name_episode = scrapy.Field()
        download_url = scrapy.Field()
        server_name_1 = scrapy.Field()
        server_url_1 = scrapy.Field()
        server_name_2 = scrapy.Field()
        server_url_2 = scrapy.Field()
        server_name_3 = scrapy.Field()
        server_url_3 = scrapy.Field()
        server_name_4 = scrapy.Field()
        server_url_4 = scrapy.Field()
        server_name_5 = scrapy.Field()
        server_url_5 = scrapy.Field()
        server_name_6 = scrapy.Field()
        server_url_6 = scrapy.Field()
        server_name_7 = scrapy.Field()
        server_url_7 = scrapy.Field()
        server_name_8 = scrapy.Field()
        server_url_8 = scrapy.Field()
        server_url_9 = scrapy.Field()


class AjarAnilistItem(scrapy.Item):
	    image_url = scrapy.Field()


class AjarWallAlphaItem(scrapy.Item):
			image_url = scrapy.Field()
			image_tags = scrapy.Field()
			image_type = scrapy.Field()

