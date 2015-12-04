from __future__ import print_function
import six


class Resource(object):
    """Abstract base class wrapper for a dict to give it an object interface.

    >>> d = {'foo': 1, 'bar': {'a': 3, 'b': 4}}
    >>> MyResource = type('MyResource', (Resource,), {'_load': lambda: 0})
    >>> o = MyResource(d)

    #>>> o
    {foo : 1, bar : {a : 3, b : 4}}

    >>> o.foo
    1
    >>> o["foo"]
    1
    >>> o.bar.a
    3

    Heavily inspired by: http://stackoverflow.com/a/6573827/577199
    """
    def __init__(self, d):
        self._update(d)

    def _update(self, data):
        """Update the object with new data."""
        for k, v in six.iteritems(data):
            new_value = v
            if isinstance(v, dict):
                new_value = type(self)(v)
            elif isinstance(v, list):
                new_value = [(type(self)(e) if isinstance(e, dict) else e)
                             for e in v]
            setattr(self, k, new_value)

    def __getattr__(self, val):
        """Try to get an attribute. On failure, load the object in full
        and try again."""
        return self.__dict__[val]

    def __getitem__(self, val):
        return self.__dict__[val]

    def __repr__(self):
        """Make the resource appear like a dict."""
        return '{%s}' % str(', '.join('%s : %s' % (k, repr(v)) for
            (k, v) in six.iteritems(self.__dict__)))


class Athlete(Resource):
    """Class for an athlete on roster"""
    pass
