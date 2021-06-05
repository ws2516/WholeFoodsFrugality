import requests
import bs4
import pandas as pd
from bs4 import BeautifulSoup

#must be selenium run periodically that attaches to gspread, use the selenium to update the xhr maybe?

def get_page_number(page_url):
	page_sourced = requests.get(url, timeout=10, headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9,fr;q=0.8,ro;q=0.7,ru;q=0.6,la;q=0.5,pt;q=0.4,de;q=0.3',
	'cache-control': 'max-age=0',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}).content
	html_content = BeautifulSoup(page_sourced, "html.parser")
	print(html_content)
	final_page_number = html_content.find_all('a _ngcontent-serverapp-c188')
	return final_page_number


def name_of_item(url):
	page_sourced = requests.get(page_url, headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,fr;q=0.8,ro;q=0.7,ru;q=0.6,la;q=0.5,pt;q=0.4,de;q=0.3',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}).content
	html_content = BeautifulSoup(page_sourced, "html.parser")
	sale_item_names = html_content.find_all('a', class_="shelfProductTile-descriptionLink")
	sale_item_names = [i.text for i in sale_item_price]
	return sale_item_names

url ="https://www.woolworths.com.au/shop/browse/specials/half-price"
print(get_page_number(url))

'''
    sale_item_titles = [i.text for i in sale_items]
    sale_item_price = html_content.findAll('span', class_="w-sales-tile__sale-price w-header3 w-bold-txt")
    sale_item_prices = [i.text for i in sale_item_price]
    return pd.DataFrame({'Sale Item': sale_item_titles, 'Sale Price':sale_item_prices, 'Store':[name]*len(sale_item_prices)})
    #?pageNumber=2
    _ngcontent-serverapp-c188
'''