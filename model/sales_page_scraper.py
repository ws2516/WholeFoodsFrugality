import requests
import bs4
import pandas as pd
from bs4 import BeautifulSoup

def items_on_sale(page_url):
    page_sourced = requests.get(page_url).content
    html_content = BeautifulSoup(page_sourced, "html.parser")
    sale_items = html_content.findAll('h4', class_="w-sales-tile__product")
    sale_item_titles = [i.text for i in sale_items]
    sale_item_price = html_content.findAll('span', class_="w-sales-tile__sale-price w-header3 w-bold-txt")
    sale_item_prices = [i.text for i in sale_item_price]
    return pd.DataFrame({'Sale Item': sale_item_titles, 'Sale Price':sale_item_prices})