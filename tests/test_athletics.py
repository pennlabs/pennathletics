from nose.tools import ok_, eq_
from pennathletics.athletes import get_roster, get_player


class TestAthletics():
    def test_roster(self):
        ok_(get_roster("M_Basketball", 2015) != [])

    def test_player_empty(self):
        ok_(get_player("M_Basketball", 2014) != [])

    def test_player_number(self):
        eq_(get_player("M_Basketball", 2013, no=1)[0].height, '6-2')
