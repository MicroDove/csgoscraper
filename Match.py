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
        return self

    def __eq__(self, other):
        time_margin_of_error = dt.timedelta(minutes=-30) <= (self.start - other.start) <= dt.timedelta(minutes=30)
        if (self.team1 == other.team1 and self.team2 == other.team2) and (self.start == other.start or time_margin_of_error):
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
    m1 = Match(dt.datetime(2020, 4, 20), "Swole Patrol", "Fnatic", "EGB", 1.61, 2.1)
    m1.timeleft()
    print(m1)
    print(m1.timeleft())
    m2 = Match(dt.datetime(2020, 4, 20), "Swole Patrol", "Fnatic", "EGB", 1.61, 2.1)
    print(m1 == m2)
    m3 = Match(dt.datetime(2020, 5, 20), "Swole Patrol", "Fnatic", "GG", 2.1, 1.61)
    print(m1 == m3)
    print(m1+m3)
    m1+=m3
    print(m1.odds)
    m1 = Match(dt.datetime(2020, 4, 20, 8), "Swole Patrol", "Fnatic", "EGB", 1.61, 2.1)
    m4 = Match(dt.datetime(2020, 4, 20, 7, 59, 59), "Swole Patrol","Fnatic", "GG", 2.1, 1.61)
    print(m1)
    print(m4)
    print(m4 == m1)
    print(m1 == m4)


