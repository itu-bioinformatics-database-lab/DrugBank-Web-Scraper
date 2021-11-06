# DrugBank-Web Scraper

import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Initialize the driver
chrome_driver_path = "D:\Development\Python\Web Scarping\WebDriver\chromedriver.exe" # Change to your local driver location

# Options for CloudFlare bypass
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)

# Delay time
delay = 120

driver.get("https://go.drugbank.com/pharmaco/metabolomics")
time.sleep(delay)

with open("page_markup.html", "w", encoding="utf-8") as file:
    file.write(driver.page_source)

# try:
#     WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'card-body')))
# except TimeoutException:
#     print('Loading exceeds delay time')
#     #break
# else:
#     with open("page_markup.html", "w", encoding="utf-8") as file:
#         file.write(driver.page_source)
# finally:
#     driver.quit()