from Match import Match

from bs4 import BeautifulSoup
from selenium import webdriver
import time as Time
from datetime import datetime, date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


def scrapeBW():
    driver = webdriver.Chrome("./chromedriver")
    wait = WebDriverWait(driver, 4)
    driver.get('https://sports.betway.com/en/sports/sct/esports/cs-go')

    # driver.find_element_by_xpath('//*[@class="arrowIcon icon-arrow-right"]').click() <--- this one right here officer

    Time.sleep(5)
    soup = BeautifulSoup(driver.page_source,  features="html.parser")

    days = soup.find_all("div", class_="collapsablePanel alternativeHeaderBackground")

    match_list = []
    for d in days:
        day = d.find_all("div", class_="collapsablePanel")
        for dd in day:
            title = dd.find("div", class_="titleText")
            matches = dd.find_all("div", class_="oneLineEventItem")
            for match in matches:
                try:
                    time_text = match.find("div", class_="oneLineDateTime").text
                    time = datetime.strptime(time_text, '%H:%M').time()
                    matchtime = datetime.combine(date.today(), time)
                    team1name = match.find("span", class_="teamNameFirstPart teamNameHomeTextFirstPart")
                    if team1name == None:
                        team1name = match.find("span", class_="teamNameFirstPart teamNameHomeTextFirstPart smallFont")
                    team1name = team1name.text
                    team2name = match.find("span", class_="teamNameFirstPart teamNameAwayTextFirstPart")
                    if team2name == None:
                        team2name = match.find("span", class_="teamNameFirstPart teamNameAwayTextFirstPart smallFont")
                    team2name = team2name.text
                    odds = match.find_all("div", class_="odds")
                    team1odds = odds[0].text
                    team2odds = odds[1].text
                    # print(f"Time: {matchtime} Team 1: {team1name} odds: {team1odds} Team 2: {team2name} odds: {team2odds}")
                    match_list.append(Match(matchtime, team1name, team2name, "GG", team1odds, team2odds))
                except:
                    continue
    return match_list

# l = scrapeBW()
# for i in l:
#     print(i)
