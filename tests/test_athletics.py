from nose.tools import ok_, eq_
from pennathletics.athletes import get_roster, get_player


class TestAthletics():
    def test_roster(self):
        ok_(get_roster("m-baskbl", 2015) != [])

    def test_player_empty(self):
        ok_(get_player("m-baskbl", 2014) != [])

    def test_player_number(self):
        eq_(get_player("m-baskbl", 2013, jersey=1)[0].height, "6'2\"")

    def test_player_hometown(self):
        player = get_player("m-baskbl", 2012, homeTown="Belfast, Ireland")[0]
        eq_(player.weight, '210 lbs')

    def test_player_softball(self):
        # 19 players on the 2013 softball team
        eq_(len(get_roster("w-softbl", 2013)), 19)
