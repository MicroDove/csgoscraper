from scrapeEGB import scrapeEGB
from scrapeCSGL import scrapeCSGL
from scrapeTP import scrapeTP
from scrapeGG import scrapeGG
from scrapeBW import scrapeBW

def matchtable():
    match_table = dict()
    big_list = [scrapeTP(), scrapeGG(), scrapeBW()]
    for i in big_list:
        if i == None:
            big_list.remove(i)
    big_list.sort(key=len)
    for l in big_list:
        for match in l:
            h = hash(match)
            if h in match_table:
                match_table[h] += match
            else:
                match_table[h] = match
    return match_table
