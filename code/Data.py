from Utils import csv, map, kap
from Row import Row
from Cols import Cols


class Data:
    def __init__(self, src={}):
        self.rows = list()
        self.cols = None
        if type(src) == str:
            csv(src, self.add)
        else:
            map(src, self.add)

    def add(self, t):
        if not self.cols:
            self.cols = Cols(t)
        else:
            if type(t) == list:
                t = Row(t)
                self.cols.add(t)
                self.rows.append(t)

    def clone(self, t, data):
        data = Data(list(self.cols.names))
        map(t, self.add)
        return data

    def stats(self, cols, nPlaces, what='mid'):
        def fun(k, col):
            return col.rnd(getattr(col, what)(), nPlaces), col.txt

        return kap(cols, fun)
