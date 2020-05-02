from bs4 import BeautifulSoup
from selenium import webdriver
import time as Time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer

def scrapeEGB():
    driver = webdriver.Chrome("./chromedriver")
    wait = WebDriverWait(driver, 4)
    driver.get('https://egb.com/play/simple_bets')

    driver.find_element_by_xpath('//*[@class="filters__link-clear"]').click()
    driver.find_element_by_xpath('//*[@class="field__invisible"]').click()


    Time.sleep(5)
    soup = BeautifulSoup(driver.page_source,  features ="html.parser")

    matches = soup.find_all("div", class_="table-bets__content-row")
    for match in matches:
        date = match.find_all("span", data="date")
        if not len(date):
            # if match has already started skip grabbing the data
            pass
        else:
            # grab the data
            date = date[0].get_text()
            time = match.find_all("span", data="time")[0].get_text()
            matchtime = "{} {} UTC".format(date, time)
            team1name = match.find_all("div", class_="table-bets__player1")[0].get_text()
            team2name = match.find_all("div", class_="table-bets__player2")[0].get_text()
            odds = match.find_all("div", class_="table-bets__odds")
      
            team1odds = odds[0].get_text()
            team2odds = odds[1].get_text()
            print("Time: {:30} Team 1: {:15} odds: {:5} Team 2: {:15} odds: {:5}".format(matchtime, team1name, team1odds, team2name, team2odds))
     
# driver.find_element_by_xpath('//*[@class="filters__link-clear"]').click()
scrapeEGB()