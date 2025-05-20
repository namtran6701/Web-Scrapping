import scrapy
from my_scraper.items import SalesFactoryItem


class SalesfactorySpiderSpider(scrapy.Spider):
    name = "salesfactory_spider"
    allowed_domains = ["salesfactory.com"]
    start_urls = ["https://salesfactory.com/"]

    def parse(self, response):
        item = SalesFactoryItem()
        item['page_content'] = response.body.decode('utf-8')
        yield item
