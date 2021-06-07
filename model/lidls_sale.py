import requests
import bs4
import pandas as pd
import orjson
from bs4 import BeautifulSoup
import datetime
from datetime import datetime

def datify(date_string):
	splitter = date_string.split('-')
	month = int(splitter[1])
	day = int(splitter[2][:2])
	return (month, day)
	

def items_on_sale():
	page_url = "https://mobileapi.lidl.com/v1/specials?storeId=US01053"
	page_sourced = requests.get(page_url, timeout=10, headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9,fr;q=0.8,ro;q=0.7,ru;q=0.6,la;q=0.5,pt;q=0.4,de;q=0.3',
	'cache-control': 'max-age=0',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}).content
	html_content = orjson.loads(page_sourced)
	listings = html_content['current']
	dollar_price, name_items = [], []
	for i in listings:
		today = datify(str(datetime.today()))
		if datify(i['startDate']) < today < datify(i['endDate']): #compare the date here
			for j in i['products']:
				name_items.append(j['name'])
				dollar_price.append(j['price']['currentPrice']['value'])
	return pd.DataFrame({'Sale Item': name_items, 'Sale Price':dollar_price})
