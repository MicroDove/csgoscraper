import datetime as dt

class Match:
    def __init__(self, start, team1, team2, bookmaker, oddsteam1):
        self.start = start
        self.team1 = team1
        self.team2 = team2
        self.odds = dict()
        self.odds[bookmaker] = oddsteam1
        # keys = bookmaker
        # values = odds for a bookmaker
    def __str__(self):
        return "{} vs {} Start: {}".format(self.team1, self.team2, self.start)

    def timeleft(self):
        # returns timedelta object representing how long before the game starts
        return dt.datetime.now() - self.start


if __name__ == "__main__":        
    # here is an example match object
    m = Match(dt.datetime(2020, 4, 20), "Swole Patrol", "Fnatic", "EGB", 1.61)
    m.timeleft()
    print(m)
    print(m.timeleft())


