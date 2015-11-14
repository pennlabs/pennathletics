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
    
def get_player(sport, year, name="", no=-1):
    """Returns players with given attributes. *Sport and Year are required"""
    
    potential_list = get_roster(sport, year)
    list_to_return = [] 
    index_in_list  = 0
    passed_num     = 0 

    for i in range(0, len(potential_list)):
        if potential_list[i].no == '':
            passed_num = ''
        else: 
    	    passed_num = int(potential_list[i].no)

        if ((name == "" or name == potential_list[i].name) & 
            (no == -1 or passed_num == no) & 
            (no >= 0 or name != "")):
                list_to_return.append(potential_list[i])
        index_in_list += 1
    return list_to_return

print (get_player('M_Basketball', 2015, no=0))