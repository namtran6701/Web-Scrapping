import scrapy
# from my_scraper.items import RedbookIndexItem # Old item
# from my_scraper.items import GeneralPageContentItem # Old item
from my_scraper.items import RagPageItem # New item for RAG


class SalesfactorySpiderSpider(scrapy.Spider):
    name = "salesfactory_spider"
    allowed_domains = ["salesfactory.com"]
    start_urls = ["https://www.salesfactory.com/"]

    def parse(self, response):
        item = RagPageItem()
        item['source_url'] = response.url
        item['title'] = response.css('title::text').get() 

        # Attempt to extract main content - THIS WILL LIKELY NEED ADJUSTMENT
        # Common selectors for main content: 'main', 'article', 'div.content', 'div#main'
        # You'll need to inspect salesfactory.com to find the correct selector
        main_content_selectors = ['main', 'article', 'div.content', 'div#main-content', 'div.page-content']
        main_content_text = ''
        for selector in main_content_selectors:
            content_html = response.css(selector)
            if content_html:
                # Extract all text nodes, join them, and clean up whitespace
                main_content_text = ' '.join(content_html.xpath('.//text()').getall()).strip()
                main_content_text = ' '.join(main_content_text.split()) # Normalize whitespace
                break # Found content, no need to check other selectors
        
        if not main_content_text:
            # Fallback if no specific main content selector worked: get all body text
            # This is less ideal but better than nothing. You might want to log this.
            self.logger.warning(f"Could not find specific main content for {response.url}, falling back to body text.")
            body_text = ' '.join(response.xpath('//body//text()').getall()).strip()
            main_content_text = ' '.join(body_text.split())

        item['main_content_text'] = main_content_text

        yield item

        # Find all links on the page and follow them
        for next_page_url in response.css('a::attr(href)').getall():
            if next_page_url is not None:
                # Potentially add filtering here to only follow relevant links
                yield response.follow(next_page_url, callback=self.parse)
