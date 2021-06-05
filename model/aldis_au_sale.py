import requests
import bs4
import pandas as pd
from bs4 import BeautifulSoup

def items_on_sale():
	page_url = "https://www.aldi.com.au/en/groceries/price-reductions/"
	page_sourced = requests.get(page_url, timeout=10, headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9,fr;q=0.8,ro;q=0.7,ru;q=0.6,la;q=0.5,pt;q=0.4,de;q=0.3',
	'cache-control': 'max-age=0',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}).content
	html_content = BeautifulSoup(page_sourced, "html.parser")
	names_items = [i.text.strip() for i in html_content.find_all('div', class_="box--description--header")]
	dollar_price = [i.text.strip() for i in html_content.find_all('span', class_="box--saveing")]
	return pd.DataFrame({'Sale Item': names_items, 'Sale Price':dollar_price})


