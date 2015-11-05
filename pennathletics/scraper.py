import requests
from bs4 import BeautifulSoup
import re

SPORTS = {
    'M_Baseball' : {
        'SPID'  : 548,
        'SPSID' : 8834
    },
    'M_Basketball' : {
        'SPID'  : 539,
        'SPSID' : 8627
    },
    'M_Track_Cross' : {
        'SPID'  : 542,
        'SPSID' : 8699
    },
    'M_Fencing' : {
        'SPID'  : 607,
        'SPSID' : 10603
    },
    'M_Football' : {
        'SPID'  : 537,
        'SPSID' : 8571
    },
    'M_Sprint_Football' : {
        'SPID'  : 612,
        'SPSID' : 10618
    },
    'M_Golf' : {
        'SPID'  : 550,
        'SPSID' : 8895
    },
    'M_Lacrosse' : {
        'SPID'  : 544,
        'SPSID' : 8745
    },
    'M_Heavy_Rowing' : {
        'SPID'  : 610,
        'SPSID' : 10659
    },
    'M_Light_Rowing' : {
        'SPID'  : 613,
        'SPSID' : 10647
    },
    'M_Soccer' : {
        'SPID'  : 604,
        'SPSID' : 10672
    },
    'M_Squash' : {
        'SPID'  : 605,
        'SPSID' : 10685
    },
    'M_Swimming' : {
        'SPID'  : 611,
        'SPSID' : 10698
    },
    'M_Tennis' : {
        'SPID'  : 552,
        'SPSID' : 8927
    },
    'M_Wrestling' : {
        'SPID'  : 543,
        'SPSID' : 8720
    },
    'W_Basketball' : {
        'SPID'  : 540,
        'SPSID' : 8650
    },
    'W_Track_Cross' : {
        'SPID'  : 558,
        'SPSID' : 10758
    },
    'W_Fencing' : {
        'SPID'  : 608,
        'SPSID' : 10715
    },
    'W_Hockey' : {
        'SPID'  : 609,
        'SPSID' : 10583
    },
    'W_Golf' : {
        'SPID'  : 551,
        'SPSID' : 8903
    },
    'W_Gymnastics' : {
        'SPID'  : 545,
        'SPSID' : 8763
    },
    'W_Lacrosse' : {
        'SPID'  : 554,
        'SPSID' : 8966
    },
    'W_Rowing' : {
        'SPID'  : 555,
        'SPSID' : 8993
    },
    'W_Soccer' : {
        'SPID'  : 541,
        'SPSID' : 8673
    },
    'W_Softball' : {
        'SPID'  : 549,
        'SPSID' : 8856
    },
    'W_Squash' : {
        'SPID'  : 606,
        'SPSID' : 10741
    },
    'W_Swimming' : {
        'SPID'  : 546,
        'SPSID' : 8790
    },
    'W_Tennis' : {
        'SPID'  : 553,
        'SPSID' : 8943
    },
    'W_Volleyball' : {
        'SPID'  : 538,
        'SPSID' : 8606
    }
}


ROSTER_URL = 'http://www.pennathletics.com/SportSelect.dbml?&DB_OEM_ID=1700&SPID={}&SPSID={}&Q_SEASON={}'

# requests.get("http://www.pennathletics.com/SportSelect.dbml?&DB_OEM_ID=1700&SPID=540&SPSID=8650")

def getRoster(sport, year):
    """Return a roster of players.
    :param sport: string value of sport.
    """
    r = requests.get(ROSTER_URL.format(SPORTS[sport]['SPID'],SPORTS[sport]['SPSID'],year))
    parsed = BeautifulSoup(r.text, "html.parser")
    info_table = parsed.find_all('table')[2]
    

    # print(parsed)
    # print(ROSTER_URL.format(SPORTS[sport]['SPID'],SPORTS[sport]['SPSID'],year))
    print(info_table)

    
# print(SPORTS['W_Swimming']['SPID'])
getRoster('W_Basketball',2015)
