from bs4 import BeautifulSoup
from selenium import webdriver
import time as Time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer


def scrapeTP():
    driver = webdriver.Chrome("./chromedriver")
    wait = WebDriverWait(driver, 4)
    driver.get('https://thunderpick.com/en/esports/csgo?list=upcoming')

    Time.sleep(5)
    soup = BeautifulSoup(driver.page_source,  features="html.parser")

    matches = soup.find_all("div", class_="thp-matches-page__match-row-container")

    # test = open('test.html', 'w')
    # print(matches[0].prettify(), file=test)
    # test.close()

    for match in matches:
        #time = match.find_all("div", class_="t--center match-row--large__time-to-start visible")
        matchtime = 0
        teams = match.find_all("div", class_="match-row--large__participant-name")
        team1name = teams[0].get_text()
        team2name = teams[1].get_text()
        odds = match.find_all("button", class_="odds-button odds-button--theme-primary odds-button--variant-dark")
        team1odds = odds[0].get_text()
        team2odds = odds[1].get_text()
        print("Time: {:30} Team 1: {:15} odds: {:5} Team 2: {:15} odds: {:5}".format(matchtime, team1name, team1odds, team2name, team2odds))

scrapeTP()
