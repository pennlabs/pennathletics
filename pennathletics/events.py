from munch import munchify
import requests
import arrow

EVENTS_URL = ("http://www.pennathletics.com/v3/events?page=1&limit=40"
              "&timezone=America/New_York&sort_direction=ASC"
              "&sub_types=SportEvent,MediaEvent&sort=eventDate&start_date={}")


def events():
    """Fetch events for the current day"""
    date = arrow.now().format('YYYY-MM-DD')
    uri = EVENTS_URL.format(date)
    return munchify(requests.get(uri).json())
