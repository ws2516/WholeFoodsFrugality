import requests
import bs4
import pandas as pd
from bs4 import BeautifulSoup

def items_on_sale():
	page_url = "https://www.aldi.us/en/weekly-specials/this-weeks-aldi-finds/"
	page_sourced = requests.get(page_url, timeout=10, headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9,fr;q=0.8,ro;q=0.7,ru;q=0.6,la;q=0.5,pt;q=0.4,de;q=0.3',
	'cache-control': 'max-age=0',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}).content
	html_content = BeautifulSoup(page_sourced, "html.parser")
	names_items = [i.text.strip() for i in html_content.find_all('div', class_="box--description--header")]
	in_store = [i.text.strip()=='*see price in store' for i in html_content.find_all('span', class_="box--amount")]
	min_names = []
	for i in range(len(names_items)):
		if not in_store[i]:
			min_names.append(names_items[i])
		else:
			continue
	dollar_price = [i.text.strip() for i in html_content.find_all('span', class_="box--value")]
	cent_price = [i.text.strip() for i in html_content.find_all('span', class_="box--decimal")]
	price_now = [dollar_price[i]+cent_price[i] for i in range(len(cent_price))]
	return pd.DataFrame({'Sale Item': min_names, 'Sale Price':price_now})
