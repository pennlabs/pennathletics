from __future__ import print_function #PYTHON 3 BABY
import models, parse
import scraper as s

def get_roster(sport, year):
    roster = []
    raw = s.scrape_roster(sport, year)
    for person in raw:
        roster.append(
            models.Athlete(
            person[0],
            person[1],
            person[2],
            parse.ht_feet_to_inches(person[3]),
            person[4],
            person[5],
            parse.parse_hometown(person[6]))
        )
    return roster
        
    
# print(get_roster('M_Basketball',2015))