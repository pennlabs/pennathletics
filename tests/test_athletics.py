from nose.tools import ok_, eq_
from pennathletics.athletes import get_roster, get_player
from pennathletics.scraper import get_schedule

class TestAthletics():
    def test_roster(self):
        ok_(get_roster("M_Basketball", 2015) != [])

    def test_player_empty(self):
        ok_(get_player("M_Basketball", 2014) != [])

    def test_player_number(self):
        eq_(get_player("M_Basketball", 2013, no=1)[0].height, '6-2')

    def test_player_hometown(self):
        eq_(get_player("M_Basketball",
                2002, Hometown="Germantown,Md. (DeMatha)")[0].weight, 215)

    def test_player_softball(self):
        ok_(get_roster("W_Softball", 2002) == [])

    def test_schedule(self):
        ok_(get_schedule("M_Soccer", 2011) != [])
