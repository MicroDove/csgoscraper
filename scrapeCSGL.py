from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time as Time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer
def scrapeCSGL():
        driver = webdriver.Chrome("./chromedriver")
        wait = WebDriverWait(driver, 4)
        driver.get('https://csgolounge.com/')
        Time.sleep(5)

        soup = BeautifulSoup(driver.page_source,  features ="html.parser")
        matches = soup.find_all("div", class_="lounge-bets-items__item sys-betting")
        toreturn = []

        for match in matches:
                # process text
                matchtext = match.get_text().strip()
                info1 = matchtext.split("         ")
                temp = info1[1].split("   ")
                if(len(temp) < 2):
                        continue
                team1name = temp[0]
                team1odds = temp[1][1:]
                
                
                temp = info1[-1].split("       ")
                temp = temp[1].split("   ")
                team2name = temp[0]
                if(len(temp) < 2):
                        continue
                team2odds = temp[1][1:]

                matchtime = info1[0].split("  ")[0]

                # at this poit all values are valid
                print("Time: {:30} Team 1: {:15} odds: {:5} Team 2: {:15} odds: {:5}".format(matchtime, team1name, team1odds, team2name, team2odds))
                
                # toreturn.append("CSGL {} {} {} {} {} {}".format(info[0]))

#scrapeCSGL()