from munch import munchify
import requests
import arrow
from . import BASE_URL

EVENTS_URL = (BASE_URL + "/events?page=1&limit=40&timezone=America/New_York"
              "&sort_direction=ASC&sub_types=SportEvent,MediaEvent"
              "&sort=eventDate&start_date={}")

SCHEDULE_URL = (BASE_URL + "/events?page=1&limit=30&timezone=America/New_York"
                "&sort_direction=ASC&sub_types=SportEvent,MediaEvent"
                "&sort=eventDate&sport_codes={}&include_paging=true"
                "&map_method=map_schedule&seasons={}")


def events():
    """Fetch events for the current day"""
    date = arrow.now().format('YYYY-MM-DD')
    uri = EVENTS_URL.format(date)
    return munchify(requests.get(uri).json())


def get_schedule(sport_code, year):
    """Get the yearly schedule for a sport code given year in YYYY format"""
    uri = SCHEDULE_URL.format(sport_code, year)
    data = requests.get(uri).json()["content"]
    return munchify(data)
