from Match import Match

from bs4 import BeautifulSoup
from selenium import webdriver
import time as Time
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

def scrapeTP():
    driver = webdriver.Chrome("./chromedriver")
    wait = WebDriverWait(driver, 4)
    driver.get('https://thunderpick.com/en/esports/csgo?list=upcoming')

    Time.sleep(3)
    soup = BeautifulSoup(driver.page_source,  features="html.parser")

    matches = soup.find_all("div", class_="thp-matches-page__match-row-container")

    match_list = []
    for match in matches:
        try:
            time_set = match.find_all("div", class_="t--center match-row--large__time-to-start visible")
            time_to_match = [i.contents[0] for i in time_set]
            times_to_match = time_to_match[0].split(':')
            time = datetime.now().replace(microsecond=0) + timedelta(hours=int(times_to_match[0]), minutes=int(times_to_match[1]), seconds=int(times_to_match[2]))
            matchtime = time
            teams = match.find_all("div", class_="match-row--large__participant-name")
            team1name = teams[0].get_text()
            team2name = teams[1].get_text()
            odds = match.find_all("button", class_="odds-button odds-button--theme-primary odds-button--variant-dark")
            team1odds = odds[0].get_text()
            team2odds = odds[1].get_text()
            # print(f"Time: {matchtime} Team 1: {team1name} odds: {team1odds} Team 2: {team2name} odds: {team2odds}")
            match_list.append(Match(matchtime, team1name, team2name, "TP", team1odds, team2odds))
        except:
            continue
    return match_list

# l = scrapeTP()
# print(len(l)) 
