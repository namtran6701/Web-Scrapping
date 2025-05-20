import scrapy
# from my_scraper.items import SalesFactoryItem # Old import
from my_scraper.items import GeneralPageContentItem # New import


class SalesfactorySpiderSpider(scrapy.Spider):
    name = "salesfactory_spider"
    allowed_domains = ["salesfactory.com"]
    start_urls = ["https://salesfactory.com/"]

    def parse(self, response):
        # item = SalesFactoryItem() # Old item instantiation
        item = GeneralPageContentItem() # New item instantiation
        item['page_content'] = response.body.decode('utf-8')
        item['source_url'] = response.url # Populate the source URL
        yield item
