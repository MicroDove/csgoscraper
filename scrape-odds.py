from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
class scraper():

    def __init__(self):
        self.session = HTMLSession()
        self.r = self.session.get('https://egb.com/play/simple_bets')
        self.r.html.render()
        result = self.r.html.search("MAD Lions")
        print(result.text)
        print('__init__ called')

    def parsedata(self):
        pass
        # self.res = requests.get(self.url)                                    
        # self.soup = BeautifulSoup(self.res.text,  features ="html.parser")                     
        # self.matches = self.soup.find_all("div", class_="grid-inner")
        # print(self.matches)
        # for item in self.matches:
        #     print(item)
        # for self.items in self.table:

        #     self.teamname = self.items.find("div", class_="team-name").get_text().strip()
        #     print(self.teamname) 
        #     odds = self.items.find("td", class_="odds").get_text().strip()
        #     print(odds) 
            

Scrape = scraper()
Scrape.parsedata()