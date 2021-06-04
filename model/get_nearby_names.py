import requests
import selenium
import time
import webdriver_manager
import bs4
import pandas as pd
from bs4 import BeautifulSoup
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from webdriver_manager.chrome import ChromeDriverManager

def get_list_of_names(cityname):
    if True:
    	chrome_options = Options()
    	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    	chrome_options.add_argument("--headless")
    	chrome_options.add_argument("--disable-dev-shm-usage")
    	chrome_options.add_argument("--no-sandbox")
    	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    	driver.get("https://www.wholefoodsmarket.com/sales-flyer")
    	inputElement = driver.find_element_by_id("store-finder-search-bar")
    	inputElement.send_keys(str(cityname))
    	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "wfm-search-bar--list_item")))
    	saved =  driver.page_source
    	driver.close()
    	return saved
    else:
    	return "Oops, there does not seem to be a Whole Foods near you."

def get_names_nearby(page_sourced):
    if page_sourced == "Oops, there does not seem to be a Whole Foods near you.":
        return ["Oops, there does not seem to be a Whole Foods near you."]
    html_content = BeautifulSoup(page_sourced, "html.parser")
    desired_class = [i.find('span').text for i in html_content.find_all('li', class_="wfm-search-bar--list_item")]
    return desired_class


def on_input_run(string):
    return (get_names_nearby(get_list_of_names(string)))
