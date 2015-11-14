from __future__ import print_function

# TODO
# create resource #

# TODO
# athlete inherits from resource #


class Athlete(object):
    """Class for an athlete on roster"""

    def __init__(self, no, name, pos, ht, wt, yr, hometown):
        self.no       = no
        self.name     = name
        self.pos      = pos
        self.wt       = wt
        self.yr       = yr
        self.hometown = hometown

    @property
    def weight(self):
        # return ft_to_inches(self.weight)
        pass

    def __repr__(self):
        return "Athlete #{}, {},".format(self.no, self.name)
