import csv

class PropubPipeline(object):

	def __init__(self):
		self.myCSV = csv.writer(open('C:\Users\jjackovich\Desktop\propub.csv', 'wb'))
		self.myCSV.writerow(['payee', 'link', 'city', 'state', 'company', 'amount'])
		
	def process_item(self, item, spider):
		self.myCSV.writerow([item['payee'][0].encode('utf-8'), 
		item['link'][0].encode('utf-8'), 
		item['city'][0].encode('utf-8'), 
		item['state'][0].encode('utf-8'),
		item['company'][0].encode('utf-8'),
		item['amount'][0].encode('utf-8')])
		return item
