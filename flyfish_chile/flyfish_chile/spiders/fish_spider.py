from scrapy import Spider
from scrapy.selector import Selector
from flyfish_chile.items import FlyfishChileItem

class FishSpider(Spider):
    name = "fish"
    allowed_domains = ["moldychum.com"]
    start_urls = [
        "http://www.moldychum.com/home-old/",
    ]

    def parse(self, response):
        # headers = hxs.selector('//a[contains(@href, "")]/@href').extract()
        headers = Selector(response).xpath('//a[contains(@class,"journal-entry-navigation-current") and contains(@href,"home-old")]')
        print "TEST!!!!"
        print headers
        for head in headers:
            print "HEAD"
            print 'http://www.moldychum.com' + head.xpath('@href').extract()[0]
            # x = head.xpath('/text()').extract()

            item = FlyfishChileItem()
            # titleNode = head[0]
            item['title'] = head.xpath('text()').extract()[0]
            item['url'] = 'http://www.moldychum.com' + head.xpath('@href').extract()[0]
            yield item