from bs4 import BeautifulSoup
from selenium import webdriver
import time as Time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer


def scrapeGG():
    driver = webdriver.Chrome("./chromedriver")
    wait = WebDriverWait(driver, 4)
    driver.get('https://ggbet.com/en/counter-strike')

    driver.find_element_by_xpath('//*[@class="viewToggler__icon___M-I-X __app-Icon"]').click()

    Time.sleep(5)
    soup = BeautifulSoup(driver.page_source,  features="html.parser")

    matches = soup.find_all("div", class_="sportEventRowNew__container___1iQKC")

    test = open('test.html', 'w')
    print(matches[0].prettify(), file=test)
    test.close()

    for match in matches:
        #time = match.find_all("div", class_="t--center match-row--large__time-to-start visible")
        matchtime = 0
        teams = match.find_all("div", class_="__app-LogoTitle-name LogoTitle__name___2LTlu")
        team1name = teams[0].get_text()
        team2name = teams[1].get_text()
        odds = match.find_all("div", class_="odd__ellipsis___3b4Yk")
        if len(odds) == 0:
            continue
        team1odds = odds[0].get_text()
        team2odds = odds[1].get_text()
        print("Time: {:30} Team 1: {:15} odds: {:5} Team 2: {:15} odds: {:5}".format(matchtime, team1name, team1odds, team2name, team2odds))





scrapeGG()
