from __future__ import print_function


class Athlete(object):
    """Class for an athlete on roster"""

    def __init__(self, no, name, pos, ht, wt, yr, hometown):
        self.no       = no
        self.name     = name
        self.pos      = pos
        self.wt       = wt
        self.yr       = yr
        self.hometown = hometown

    def __repr__(self):
        return "Athlete #{}, {},".format(self.no, self.name)
