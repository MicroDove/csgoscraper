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

    Time.sleep(3)
    soup = BeautifulSoup(driver.page_source,  features="html.parser")

    days = soup.find_all("div", class_="collapsablePanel alternativeHeaderBackground")

    for d in days:
        day = d.find_all("div", class_="collapsablePanel")
        for dd in day:
            title = dd.find("div", class_="titleText")
            matches = dd.find_all("div", class_="oneLineEventItem")
            for match in matches:
                matchtime = match.find("div", class_="oneLineDateTime").text
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
                print(f"Time: {matchtime} Team 1: {team1name} odds: {team1odds} Team 2: {team2name} odds: {team2odds}")

    # for match in matches:
    #     time_set = match.find_all("div", class_="matchDateTime__date___2Hw-c")
    #     time_to_match = [(i.contents[0].text, i.contents[1]) for i in time_set]
    #     year = str(date.today().year)
    #     time_string = str(time_to_match[0][1]) + \
    #         ' '+year+' ' + str(time_to_match[0][0])
    #     matchtime = datetime.strptime(time_string, '%b %d %Y %H:%M')
    #     teams = match.find_all(
    #         "div", class_="__app-LogoTitle-name LogoTitle__name___2LTlu")
    #     team1name = teams[0].get_text()
    #     team2name = teams[1].get_text()
    #     odds = match.find_all("div", class_="odd__ellipsis___3b4Yk")
    #     if len(odds) == 0:
    #         continue
    #     team1odds = odds[0].get_text()
    #     team2odds = odds[1].get_text()
    #     print(
    #         f"Time: {matchtime} Team 1: {team1name} odds: {team1odds} Team 2: {team2name} odds: {team2odds}")

scrapeBW()
