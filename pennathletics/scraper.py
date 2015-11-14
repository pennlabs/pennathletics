import requests
from bs4 import BeautifulSoup
import sportsdata

ROSTER_URL = 'http://www.pennathletics.com/SportSelect.dbml?&DB_OEM_ID=1700&SPID={}&SPSID={}&Q_SEASON={}'

GAMES_URL = 'http://www.pennathletics.com/SportSelect.dbml?SPSID={}&SPID={}&DB_OEM_ID=1700&Q_SEASON={}'

def scrape_roster(sport, year):
    """Returns a list of lists contianing individual player information for a team.
    :param sport: string value of sport.
    :param year: 4 digit int of year.
    """
    
    roster     = []
    # import pdb; pdb.set_trace()
    r          = requests.get(ROSTER_URL.format(sportsdata.SPORTS[sport].SPID, sportsdata.SPORTS[sport].SPSID,year))
    parsed     = BeautifulSoup(r.text, "html.parser")
    info_table = parsed.find_all('table')[2].find_all('tr')

    for row in info_table:
        unparsed      = [row.find_all('td') for td in row][0] # Get all table data
        parsed    = [td.decode_contents(formatter='html').strip().replace(u'&nbsp;', '') for td in unparsed] #put it in lists, strip extraneous html
        parsed[1] = BeautifulSoup(parsed[1], "html.parser").text # the player name is nested.
        roster.append(parsed)

    roster = roster[7:] # remove header crap

    return roster

def get_schedule(sport, year):
    """Return the schedule of given year.
    :param sport: string value of sport.
    :param year: 4 digitinteger value of year.
    """
    gameData   = []
    r          = requests.get(
                    GAMES_URL.format(sportsdata.SPORTS[sport].SPSID-1, 
                    sportsdata.SPORTS[sport].SPID, 
                    year)
                 )
    parsed     = BeautifulSoup(r.text, "html.parser")
    info_table = parsed.find_all('table')[0].find_all('tr')
    for row in info_table:
        data   = [row.find_all('td') for td in row][0]
        parsed = [td.decode_contents(formatter="html").strip().replace(u'&nbsp;', '') for td in data]
        if len(parsed) > 1:
            for i in range(0, len(parsed)-1):
                print (i, len(parsed))
                parsed[i] = BeautifulSoup(parsed[i]).decode_contents(formatter="html").strip()
                gameData.append(parsed)
    return gameData
