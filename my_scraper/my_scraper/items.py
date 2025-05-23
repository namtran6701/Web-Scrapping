# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Default Scrapy item, can be removed if not used or kept as a placeholder
class MyScraperItem(scrapy.Item):
    pass

class GeneralPageContentItem(scrapy.Item):
    page_content = scrapy.Field()
    source_url = scrapy.Field() # Added to track the source
