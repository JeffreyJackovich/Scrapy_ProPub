import scrapy
from scrapy.item import Item, Field

class PropubItem(scrapy.Item):
	payee = scrapy.Field()
	link = scrapy.Field()
	city = scrapy.Field()
	state = scrapy.Field()
	company = scrapy.Field()
	amount =  scrapy.Field()
	pass
