# image_scraper/items.py

import scrapy

class ImageScraperItem(scrapy.Item):
    image_urls = scrapy.Field()
