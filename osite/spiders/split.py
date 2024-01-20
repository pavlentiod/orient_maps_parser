import scrapy
from scrapy.spiders import CrawlSpider, Rule
import pandas as pd


class SplitSpider(scrapy.Spider):
    name = "split"
    allowed_domains = ["omaps.worldofo.com"]
    start_urls = ["https://omaps.worldofo.com/" + i for i in pd.read_csv('map_links.csv')['links'].tolist()[272058:]]
    # 221869

    def parse(self, response):
        item = {
            'link':response.url,
            'name': response.css('#compnamelong::text').get(),
            'description':
                ''.join(response.xpath('//h4[text()="Map info"]/following-sibling::text()').getall()).split('\n')[
                    1].replace('\r', '').replace('\n', '').replace('\t', ''),
            'country_link': response.xpath(
                '//h4[text()="Map info"]/following-sibling::a[contains(@href,"?c=")]/@href').get(),
            'country_name': response.xpath(
                '//h4[text()="Map info"]/following-sibling::a[contains(@href,"?c=")]/text()').get(),
            'collections': response.xpath(
                '//h4[text()="Map collections"]/following-sibling::a[contains(@href,"?cid=")]/@href').getall(),
            'collection_names': response.xpath(
                '//h4[text()="Map collections"]/following-sibling::a[contains(@href,"?cid=")]/text()').getall(),
            'image': response.xpath('//h4[text()="Full map"]/following-sibling::a[1]/@href').get(),
            'popularity': response.xpath('//h4[text()="Like this?"]/following-sibling::i[1]/text()').get().split(' ')[
                0],
            'location': response.xpath('//h4[text()="Like this?"]/following-sibling::iframe/@src').get()
        }
        yield item
        # yield {'links': response.xpath('//td/div/a[contains(@href, "index")]/@href').getall()}
# 347727
# scrapy runspider split.py -o map_info_from1000.csv