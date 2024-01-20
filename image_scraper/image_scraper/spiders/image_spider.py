# image_scraper/spiders/image_spider.py
import scrapy
from image_scraper.items import ImageScraperItem



class ImageSpider(scrapy.Spider):
    name = 'image_spider'
    start_urls = ['https://eda.ru/recepty/salaty/salat-iz-krasnoj-fasoli-s-tvorozhnim-sirom-krasnim-lukom-i-sezonnim-salatom-16922']

    def parse(self, response):
        item = ImageScraperItem()
        item['image_urls'] = response.css('img::attr(src)').extract()
        yield item
