https://www.woolworths.com.au/shop/browse/specials/half-price?pageNumber=2
import requests
import bs4
import pandas as pd
from bs4 import BeautifulSoup

def get_page_number(page_url):
	page_sourced = requests.get(page_url).content
	html_content = BeautifulSoup(page_sourced, "html.parser")
	final_page_number = find_all('a', class_="paging-pageNumber")[-1].text
	return final_page_number


def name_of_item(url):
	page_sourced = requests.get(page_url).content
	html_content = BeautifulSoup(page_sourced, "html.parser")
	sale_item_names = find_all('a', class_="shelfProductTile-descriptionLink")
	sale_item_names = [i.text for i in sale_item_price]
	return sale_item_names

url = 'https://www.woolworths.com.au/shop/browse/specials/half-price' #?pageNumber=2
print(get_page_number(page_url))

'''
    sale_item_titles = [i.text for i in sale_items]
    sale_item_price = html_content.findAll('span', class_="w-sales-tile__sale-price w-header3 w-bold-txt")
    sale_item_prices = [i.text for i in sale_item_price]
    return pd.DataFrame({'Sale Item': sale_item_titles, 'Sale Price':sale_item_prices, 'Store':[name]*len(sale_item_prices)})
'''