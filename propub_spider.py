import scrapy
from propub.items import PropubItem

class propubSpider(scrapy.Spider):
    name = 'prop$'
    allowed_domains = ['projects.propublica.org']
    max_pages = 40

    def start_requests(self):
        for i in range(self.max_pages):
            yield scrapy.Request('https://projects.propublica.org/docdollars/search?page=%d' % i, callback=self.parse)

    def parse(self, response):
        for sel in response.xpath('//*[@id="payments_list"]//tr[@data-payment-id]'):
            item = PropubItem()
            item['payee'] = sel.xpath('td[@class="name_and_payee"]/a[last()]/text()').extract()
            item['link'] = sel.xpath('td[@class="name_and_payee"]/a[1]/@href').extract()
            item['city'] = sel.xpath('td[@class="city"]/text()').extract()
            item['state'] = sel.xpath('td[@class="state"]/text()').extract()
            item['company'] = sel.xpath('td[@class="company"]/text()').extract()
            item['amount'] = sel.xpath('td[@class="amount"]/text()').extract()
            yield item 
