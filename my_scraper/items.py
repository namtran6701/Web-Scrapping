import scrapy


class SalesFactoryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page_content = scrapy.Field() 