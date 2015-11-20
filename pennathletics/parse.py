"""Utilities for parsing pages"""

from collections import namedtuple
from datetime import datetime

Home = namedtuple('Home', ['town', 'school'])


def ht_feet_to_inches(ht_str):
    """Take in height in ft-in format, and return inches

    >>> ht_feet_to_inches("6-0")
    72
    """
    feet, inches = ht_str.split("-")
    return int(feet) * 12 + int(inches)


def parse_hometown(hometown_str):
    """Take in athlete's hometown and parse it into hometown and previous
    school

    >>> parse_hometown("Newport Beach, Calif. (Orange Lutheran)")
    Home(town='Newport Beach, Calif.', school='Orange Lutheran')
    """
    town, school = hometown_str.split("(")[:2]
    return Home(town[:-1], school[:-1])


def parse_date_in_schedule(dayAndMonth, time, year):
    """Will take in the values from the day of the Week, month, day, and year
    and return a python datetime object

    >>> parse_date_in_schedule("Tue, Nov 20", "8:00 PM", 2014)
    datetime.datetime(2014, 11, 20, 20, 0)
    """

    date_format = '{} {} {}{}'.format(
        dayAndMonth[5:],
        year,
        time[0:4],
        time[5:7])
    date_object = datetime.strptime(date_format, '%b %d %Y %I:%M%p')
    return date_object
