from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
#driver = webdriver.Chrome('/Users/danter.gil-marin/Downloads/chromedriver')
wait = WebDriverWait(driver, 4)
driver.get('https://csgolounge.com/')
time.sleep(5)

soup = BeautifulSoup(driver.page_source,  features ="html.parser")
matches = soup.find_all("div", class_="lounge-bets-items__item sys-betting")
for match in matches:
        print(match.get_text().strip())


# url = 'https://csgolounge.com/'

# #driver = webdriver.Firefox()
# driver = webdriver.Chrome('/Users/danter.gil-marin/Downloads/chromedriver')
# driver.implicitly_wait(10)
# driver.get(url)
# # timeout = 10
# # element_present = EC.presence_of_element_located(
# #     (By.CLASS_NAME, "lounge-bets sys-bets-block"))
# # WebDriverWait(driver, timeout).until(element_present)
# source = driver.page_source
# soup = BeautifulSoup(source,  features="html.parser")
# matches = soup.find_all("div", class_="lounge-bets-items__item sys-betting")
# for match in matches:
#     print(match.get_text().strip())
