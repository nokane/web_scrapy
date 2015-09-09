import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from flyfish_chile.items import FlyfishChileItem

class FishSpider(CrawlSpider):
    name = "fish"
    allowed_domains = ["moldychum.com"]
    start_urls = [
        "http://www.moldychum.com/home-old/",
    ]

    rules = (Rule (LinkExtractor(allow=("", ),restrict_xpaths=('//span[@class="paginationControlNextPageSuffix"]',))
    , callback="parse_page", follow= True),)

    print rules

    def parse_page(self, response):
        headers = Selector(response).xpath('//a[contains(@class,"journal-entry-navigation-current") and contains(@href,"home-old")]')
        for head in headers:
            item = FlyfishChileItem()
            item['title'] = head.xpath('text()').extract()[0]
            item['url'] = 'http://www.moldychum.com' + head.xpath('@href').extract()[0]
            yield item
