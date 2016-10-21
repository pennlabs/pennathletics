import requests
from munch import munchify
from . import BASE_URL

ROSTER_URL = BASE_URL + "/groups?include=members&sport_codes={sport}&seasons={year}"


def get_roster(sport, year):
    """Get roster, takes in sport code and year in YYYY format"""
    uri = ROSTER_URL.format(sport=sport, year=year)
    data = requests.get(uri).json()[0]["players"]
    return munchify(data)


def get_player(sport, year, **kwargs):
    """Returns players with given attributes. *Sport and Year are required

    >>> int(get_player('m-baskbl', 2015, jersey=0)[0].weight)
    225 lbs
    """
    potential_list = get_roster(sport, year)
    list_to_return = []

    for player in potential_list:
        if all(getattr(player, arg) == kwargs[arg] for arg in kwargs):
            list_to_return.append(player)

    return list_to_return
