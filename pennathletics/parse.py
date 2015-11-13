"""Utilities for parsing pages"""

from collections import namedtuple

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
    Home(town="Newport Beach, Calif.", school="Orange Lutheran")
    """
    town, school = hometown_str.split("(")[:2]
    return Home(town[:-1], school[:-1])
