from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer

driver = webdriver.Firefox("./")
wait = WebDriverWait(driver, 4)
driver.get('https://csgolounge.com/')
time.sleep(5)

soup = BeautifulSoup(driver.page_source,  features ="html.parser")
matches = soup.find_all("div", class_="lounge-bets-items__item sys-betting")
for match in matches:
        print(match.get_text().strip())

