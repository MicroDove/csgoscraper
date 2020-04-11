from datetime import *

class Match:
    def __init__(self, dateobject, timeobject, team1, team2, oddsteam1):
        self.matchdate = dateobject
        self.matchtime = timeobject
        self.team1 = team1
        self.team2 = team2
        self.odds = dict()
        # keys = bookmaker
        # values = odds for a bookmaker
    def timeleft(self):
        # there's only time left to be on the match if it starts more than an hour in the future
        if (self.matchdate - date.today() >  datetime.timedelta()) and (self.matchtime - date.today() > datetime.timedelta(hours = "1")):
            # the match is in the future
            

# here's a list of matches it's empty
# run script for each site
    # for each match on site:
        # check if our list of matches contains match
            # if yes: add bookkeeper:odds pair to this match's dict
            # if no: create new match object with odds dict containing only bookkeeper:odds
# go through list of matches
    # for each compute
