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


def scrapeGG():
    driver = webdriver.Chrome("./chromedriver")
    wait = WebDriverWait(driver, 4)
    driver.get('https://ggbet.com/en/counter-strike')

    Time.sleep(2)
    driver.execute_script("window.scrollTo(0, -100)")
    driver.find_element_by_xpath('//*[@class="viewToggler__icon___M-I-X __app-Icon"]').click()
    driver.execute_script("window.scrollTo(0, 1500)")

    Time.sleep(5)
    soup = BeautifulSoup(driver.page_source,  features="html.parser")

    matches = soup.find_all("div", class_="sportEventRowNew__container___1iQKC")

    # test = open('test.html', 'w')
    # print(matches[0].prettify(), file=test)
    # test.close()

    match_list = []
    for match in matches:
        time_set = match.find_all("div", class_="matchDateTime__date___2Hw-c")
        try:
            time_to_match = [(i.contents[0].text, i.contents[1]) for i in time_set]
        except:
            continue
        year = str(date.today().year)

        badcode = True
        try:
            if time_to_match[0][1].text == "Today":
                time_string = str(datetime.now().strftime("%b"))+' '+str(datetime.now().strftime("%d"))+' '+year+' '+str(time_to_match[0][0])
                badcode = False
        except:
            badcode = True
        if badcode:
            time_string = str(time_to_match[0][1])+' '+year+' '+str(time_to_match[0][0])

        matchtime = datetime.strptime(time_string, '%b %d %Y %H:%M')
        teams = match.find_all("div", class_="__app-LogoTitle-name LogoTitle__name___2LTlu")
        team1name = teams[0].get_text()
        team2name = teams[1].get_text()
        odds = match.find_all("div", class_="odd__ellipsis___3b4Yk")
        if len(odds) != 2:
            continue
        team1odds = odds[0].get_text()
        team2odds = odds[1].get_text()
        # print(f"Time: {matchtime} Team 1: {team1name} odds: {team1odds} Team 2: {team2name} odds: {team2odds}")
        match_list.append(Match(matchtime, team1name, team2name, "GG", team1odds, team2odds))
    return match_list

# l = scrapeGG()
# for i in l:
#     print(i)
