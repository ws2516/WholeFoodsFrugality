import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def items_on_sale(province):
    """
    TODO: to confirm if sales are dependent on store location
    """
    province_url = f'https://www.nofrills.ca/deals/all?query={province},%20Canada'
    food_url = 'https://www.nofrills.ca/deals/all?sort=relevance&category=27985'
    driver = webdriver.Chrome()   
    driver.get(province_url)

    flyer_xpath = '//*[@id="site-content"]/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/button'
    flyer_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, flyer_xpath)))
    flyer_button.click()

    food_xpath = '//*[@id="site-content"]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/ul/li[1]/button'
    food_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, food_xpath)))
    # TODO: debug and remove this timer - added because food is occasionally not clickable
    time.sleep(2)
    food_button.click()

    cookie_xpath = '//*[@id="privacy-policy"]/div/div/button'
    cookie_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, cookie_xpath)))
    cookie_button.click()

    # load all deal items 
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        try:
            more_xpath = '//*[@id="site-content"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[3]/div/button'
            more_button = driver.find_element_by_xpath(more_xpath)
            more_button.click()
        except NoSuchElementException:
            break
        
        time.sleep(2)

    # parse sales item
    sale_item_titles = list()
    sale_item_prices = list()
    sale_items = driver.find_elements_by_class_name('product-tile__details__info')

    for sale_item in sale_items:
        sale_title = sale_item.find_elements_by_class_name('product-tile__details__info__name')[0]
        sale_price = sale_item.find_elements_by_class_name('selling-price-list__item')[0]
        info = [i.text for i in sale_title.find_elements_by_css_selector('span')]
        price_info = sale_price.find_elements_by_css_selector('span') 
        sale_item_titles.append(' '.join(info))
        sale_item_prices.append(price_info[1].text)
           
    return pd.DataFrame({'Sale Item': sale_item_titles, 'Sale Price': sale_item_prices})
