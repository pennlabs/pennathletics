from .models import Athlete
from . import scraper as s


def get_roster(sport, year):
    raw = s.scrape_roster(sport, year)
    return [Athlete(player) for player in raw]


def get_player(sport, year, **kwargs):
    """Returns players with given attributes. *Sport and Year are required

    >>> int(get_player('M_Basketball', 2015, no = 0)[0].weight)
    225
    """
    potential_list = get_roster(sport, year)
    list_to_return = []

    for player in potential_list:
        if all(getattr(player, arg) == kwargs[arg] for arg in kwargs):
            list_to_return.append(player)

    return list_to_return
