import requests
import bs4
import pandas as pd
from bs4 import BeautifulSoup

def items_on_sale(page_url,name):
    page_sourced = requests.get(page_url).content
    html_content = BeautifulSoup(page_sourced, "html.parser")
    sale_items = html_content.findAll('h4', class_="w-sales-tile__product")
    sale_item_titles = [i.text for i in sale_items]
    sale_item_price = html_content.findAll('span', class_="w-sales-tile__sale-price w-header3 w-bold-txt")
    sale_item_prices = [i.text for i in sale_item_price]
    return pd.DataFrame({'Sale Item': sale_item_titles, 'Sale Price':sale_item_prices, 'Store':[name]*len(sale_item_prices)})

def get_url_from_name(name):
    df = pd.read_csv('model/ListOfStores.csv')
    return df[df['Store Name'] == 'Domain']['Store URL'].values[0]

def name_to_sale_df(name):
    url = str(get_url_from_name(name))
    sale_df = items_on_sale(url,name)
    return sale_df


def all_together(name_list):
    final_df = pd.DataFrame({'Sale Item':[],'Sale Price':[]})
    for i in name_list:
        new = name_to_sale_df(i)
        final_df = final_df.append(new)

    final = (final_df.drop_duplicates(subset='Sale Item', keep="first"))
    return final