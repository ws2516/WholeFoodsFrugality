import requests
import bs4
import pandas as pd
from bs4 import BeautifulSoup

#AU = url:  "https://www.aldi.com.au/en/groceries/price-reductions/"
#US = url:  "https://www.aldi.us/en/weekly-specials/this-weeks-aldi-finds/"

def get_names_for_item(page_url):
	page_sourced = requests.get(url, timeout=10, headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9,fr;q=0.8,ro;q=0.7,ru;q=0.6,la;q=0.5,pt;q=0.4,de;q=0.3',
	'cache-control': 'max-age=0',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}).content
	html_content = BeautifulSoup(page_sourced, "html.parser")
	names_items = [i.text.strip() for i in html_content.find_all('div', class_="box--description--header")]
	
	#fix this and we have australia 
	dollar_price = [i.text.strip() for i in html_content.find_all('span', class_="box--value")]
	cent_price = [i.text.strip() for i in html_content.find_all('span', class_="box--decimal")]
	print(dollar_price, cent_price)
	full_price = [dollar_price[i]+'.'+cent_price[i] for i in range(len(dollar_price))]
	return full_price

#url ="https://www.aldi.us/en/weekly-specials/this-weeks-aldi-finds/"
url = "https://www.aldi.com.au/en/groceries/price-reductions/"
print(get_names_for_item(url))

'''
    sale_item_titles = [i.text for i in sale_items]
    sale_item_price = html_content.findAll('span', class_="w-sales-tile__sale-price w-header3 w-bold-txt")
    sale_item_prices = [i.text for i in sale_item_price]
    return pd.DataFrame({'Sale Item': sale_item_titles, 'Sale Price':sale_item_prices, 'Store':[name]*len(sale_item_prices)})
    #?pageNumber=2
    _ngcontent-serverapp-c188
'''