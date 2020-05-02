import datetime as dt

class Match:
    def __init__(self, start, team1, team2, bookmaker, oddsteam1, oddsteam2):
        self.start = start
        self.team1 = team1
        self.team2 = team2
        self.odds = dict()
        self.odds[bookmaker] = (oddsteam1, oddsteam2)

    def __str__(self):
        return f"{self.team1} vs {self.team2} Start: {self.start} Number of Odds: {len(self.odds)}"
    
    def __add__(self, other):
        for i in other.odds:
            self.odds[i] = other.odds[i]

    def __eq__(self, other):
        if self.start == other.start and self.team1 == other.team1 and self.team2 == other.team2:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.start, self.team1, self.team2))

    def timeleft(self):
        # returns timedelta object representing how long before the game starts
        return dt.datetime.now() - self.start


if __name__ == "__main__":        
    # here is an example match object
    m = Match(dt.datetime(2020, 4, 20), "Swole Patrol", "Fnatic", "EGB", 1.61, 2.1)
    m.timeleft()
    print(m)
    print(m.timeleft())


