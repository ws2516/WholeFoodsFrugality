import requests
import bs4
import pandas as pd
from bs4 import BeautifulSoup

store_url, name = [], []
for i in range(10000,20000):
    tried = requests.get('https://www.wholefoodsmarket.com/sales-flyer?store-id='+str(i))
    parsed = BeautifulSoup(tried.content, "html.parser").findAll('h2')
    if len(store_url) > 505:
        break
    elif (tried.status_code == 200 and len(parsed)>0):
        store_name = [parsed[0].text]
        store_url += ['https://www.wholefoodsmarket.com/sales-flyer?store-id='+str(i)]
        print(store_name[-1], store_url[-1])

saved = pd.DataFrame({'Store Name':store_name, "Store URL":store_url})
saved.to_csv('WholeFoodsFrugality/ListOfStores.csv')