from munch import munchify
import requests
import arrow
from . import BASE_URL

EVENTS_URL = (BASE_URL + "/events?page=1&limit=40&timezone=America/New_York"
              "&sort_direction=ASC&sub_types=SportEvent,MediaEvent"
              "&sort=eventDate&start_date={}")


def events():
    """Fetch events for the current day"""
    date = arrow.now().format('YYYY-MM-DD')
    uri = EVENTS_URL.format(date)
    return munchify(requests.get(uri).json())
