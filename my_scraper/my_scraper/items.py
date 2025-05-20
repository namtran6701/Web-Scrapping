# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Default Scrapy item, can be removed if not used or kept as a placeholder
class MyScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# Renamed from SalesFactoryItem for general page content
class GeneralPageContentItem(scrapy.Item):
    page_content = scrapy.Field()
    source_url = scrapy.Field() # Added to track the source

# New Item for Trading Economics Redbook Index data
class RedbookIndexItem(scrapy.Item):
    last_value = scrapy.Field()
    unit = scrapy.Field()
    actual = scrapy.Field()
    previous = scrapy.Field()
    highest = scrapy.Field()
    lowest = scrapy.Field()
    dates = scrapy.Field()
    frequency = scrapy.Field()
    source_url = scrapy.Field()
