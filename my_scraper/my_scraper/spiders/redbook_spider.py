import scrapy
# from my_scraper.items import RedbookIndexItem # Old item
from my_scraper.items import GeneralPageContentItem # New item for general content


class RedbookSpiderSpider(scrapy.Spider):
    name = "redbook_spider"
    allowed_domains = ["tradingeconomics.com"]
    start_urls = ["https://tradingeconomics.com/united-states/redbook-index"]

    def parse(self, response):
        # item = RedbookIndexItem() # Old item instantiation
        item = GeneralPageContentItem() # Use GeneralPageContentItem

        # Extracting the main "Last" value and its unit
        # Looking for a prominent display, often with specific IDs or classes
        # Example: <div id="ctl00_ContentPlaceHolder1_ctl00_ctl01_Panel1" class="an-card-body">
        #              <b><span id="ctl00_ContentPlaceHolder1_ctl00_ctl01_Label1" class="an-card-value">1.8</span></b>
        #              <span id="ctl00_ContentPlaceHolder1_ctl00_ctl01_Label2" class="an-card-title an-clickable" onclick="window.location=\'/united-states/consumer-price-index-cpi\'">percent</span>
        # This structure is common on the site. For Redbook, the specific IDs might differ but class structure is often similar.
        # item['last_value'] = response.css('div.an-card-body span.an-card-value::text').get()
        # item['unit'] = response.css('div.an-card-body span.an-card-title::text').get()
        
        # Extracting data from the summary table
        # Typically, these tables have a clear structure, e.g., <tr><td>Label</td><td>Value</td></tr>
        # We'll look for rows containing specific text labels.
        # For "Actual":
        # item['actual'] = response.xpath('//tr[contains(td/text(), "Actual")]/td[2]/text()').get()
        # For "Previous":
        # item['previous'] = response.xpath('//tr[contains(td/text(), "Previous")]/td[2]/text()').get()
        # For "Highest":
        # item['highest'] = response.xpath('//tr[contains(td/text(), "Highest")]/td[2]/text()').get()
        # For "Lowest":
        # item['lowest'] = response.xpath('//tr[contains(td/text(), "Lowest")]/td[2]/text()').get()
        # For "Dates":
        # item['dates'] = response.xpath('//tr[contains(td/text(), "Dates")]/td[2]/text()').get()
        # For "Frequency":
        # item['frequency'] = response.xpath('//tr[contains(td/text(), "Frequency")]/td[2]/text()').get()
        
        item['page_content'] = response.body.decode('utf-8') # Get the entire HTML body
        item['source_url'] = response.url

        # # Strip whitespace from all extracted fields if they are not None
        # for field in item.fields:
        #     value = item.get(field)
        #     if isinstance(value, str):
        #         item[field] = value.strip()

        yield item
