from polygon import Polygon
from functools import lru_cache

class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m+1)]

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'

    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons,
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]

    def __iter__(self):
        #print('Calling Cities instance __iter__')
        return self.PolygonsIterator(self)

    class PolygonsIterator:
        def __init__(self, obj):
            # cities is an instance of Cities
            #print('Calling CityIterator __init__')
            self._obj = obj
            self._index = 3 # Min edges should be 3

        def __iter__(self):
            #print('Calling CitiyIterator instance __iter__')
            return self

        def __next__(self):
            #print('Calling __next__')
            if self._index >= self._obj._m:
                raise StopIteration
            else:
                item = Polygon(self._index, self._obj._R)
                self._index += 1
                return item
