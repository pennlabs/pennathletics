import requests
from bs4 import BeautifulSoup
from . import sportsdata

BASE_URL = 'http://www.pennathletics.com/SportSelect.dbml'
ROSTER_URL = BASE_URL + '?&DB_OEM_ID=1700&SPID={}&SPSID={}&Q_SEASON={}'
GAMES_URL = BASE_URL + '?SPSID={}&SPID={}&DB_OEM_ID=1700&Q_SEASON={}'

HEADER_ABBREVS = {
    'wt': 'weight',
    'ht': 'height',
    'yr': 'year',
    'pos': 'position'
}


def scrape_roster(sport, year):
    """Returns a list of lists contianing individual player information for a team.
    :param sport: string value of sport.
    :param year: 4 digit int of year.
    """

    roster = []
    r = requests.get(ROSTER_URL.format(sportsdata.SPORTS[
                     sport].SPID, sportsdata.SPORTS[sport].SPSID, year))
    parsed = BeautifulSoup(r.text, "html.parser")
    info_table = parsed.find_all('table')[2].find_all('tr')

    for row in info_table:
        # Get all table data
        unparsed = [row.find_all('td') for td in row][0]
        # put it in lists, strip extraneous html
        parsed = [td.decode_contents(formatter='html').strip().replace(
            '&nbsp;', '') for td in unparsed]
        # the player name is nested.
        parsed[1] = BeautifulSoup(parsed[1], "html.parser").text
        roster.append(parsed)

    # Separate headers and table data
    num_columns = len(roster[7])
    start_index = 8 - num_columns
    headers = [process_column(header[0]) for header in roster[start_index:7]] + ['Hometown']
    roster = roster[7:]

    # Create list of data dictionaries
    players = []
    for player in roster:
        player_data = {}
        for i, column in enumerate(headers):
            if '\n\t\t\t' in player[i]:
                player[i] = player[i].replace('\n\t\t\t','')
            elif (column == 'no' or column == 'weight') and player[i] != '':
                player[i] = int(player[i])
            player_data[column] = player[i]
        players.append(player_data)

    return players


def process_column(column_name):
    """Returns variable name-like column name.

    >>> process_column("Name")
    'name'

    >>> process_column("Wt.")
    'weight'

    >>> process_column("Na.")
    'na'
    """
    if column_name[-1] == '.':
        column_name = column_name[:-1]
    column_name = column_name.lower()

    if column_name in HEADER_ABBREVS:
        column_name = HEADER_ABBREVS[column_name]

    return column_name


def get_schedule(sport, year):
    """Return the schedule of given year.
    :param sport: string value of sport.
    :param year: 4 digitinteger value of year.
    """
    gameData = []
    r = requests.get(
        GAMES_URL.format(sportsdata.SPORTS[sport].SPSID - 1,
                         sportsdata.SPORTS[sport].SPID,
                         year)
    )
    parsed = BeautifulSoup(r.text, "html.parser")
    info_table = parsed.find_all('table')[0].find_all('tr')
    for row in info_table:
        data = [row.find_all('td') for td in row][0]
        parsed = [td.decode_contents(formatter="html").strip(
        ).replace('&nbsp;', '') for td in data]
        if len(parsed) > 1:
            for i in range(0, len(parsed) - 1):
                print (i, len(parsed))
                parsed[i] = BeautifulSoup(parsed[i]).decode_contents(
                    formatter="html").strip()
                gameData.append(parsed)
    return gameData
