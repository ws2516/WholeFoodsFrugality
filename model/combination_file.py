import model
from model import sales_page_scraper

def go(inputs):
    final_df = sales_page_scraper.items_on_sale("https://www.wholefoodsmarket.com/sales-flyer?store-id=10005")
    return final_df.to_html()