import requests
import bs4
import pandas as pd
import orjson
from bs4 import BeautifulSoup

def items_on_sale():
	page_url = "https://www.aldi.co.uk/api/productsearch/rr/category/Price-drops?q=%3Apopular"
	page_sourced = requests.get(page_url, timeout=10, headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9,fr;q=0.8,ro;q=0.7,ru;q=0.6,la;q=0.5,pt;q=0.4,de;q=0.3',
	'cache-control': 'max-age=0',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}).json()
	html_content = page_sourced.content
	listings = html_content['results']
	dollar_price, name_items = [], []
	for i in listings:
		name_items.append(i['name'])
		dollar_price.append(i['price'])
	return pd.DataFrame({'Sale Item': name_items, 'Sale Price':dollar_price})
