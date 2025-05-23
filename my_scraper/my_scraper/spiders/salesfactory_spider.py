import scrapy
# from my_scraper.items import RedbookIndexItem # Old item
from my_scraper.items import GeneralPageContentItem # New item for general content


class SalesfactorySpiderSpider(scrapy.Spider):
    name = "salesfactory_spider"
    allowed_domains = ["https://www.salesfactory.com/"]
    start_urls = ["https://www.salesfactory.com/"]

    def parse(self, response):
        item = GeneralPageContentItem() 
        item['page_content'] = response.body.decode('utf-8')
        item['source_url'] = response.url

        yield item
