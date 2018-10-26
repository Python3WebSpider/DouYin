import collections

HotSearch = collections.namedtuple('HotSearch', ['datetime', 'data'])
HotVideo = collections.namedtuple('HotVideo', ['datetime', 'data'])
HotEnergy = collections.namedtuple('HotVideo', ['datetime', 'data'])
HotMusic = collections.namedtuple('HotMusic', ['datetime', 'data'])
HotTrend = collections.namedtuple('HotTrend', ['datetime', 'data', 'count', 'offset'])