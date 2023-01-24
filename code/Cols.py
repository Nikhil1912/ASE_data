import re
from Sym import Sym
from Num import Num


class Cols:
    def __init__(self, t):
        self.names = t
        self.all = []
        self.klass = None
        self.x = []
        self.y = []
        for n, s in enumerate(t):
            if re.match('^[A-Z]+', s):
                col = Num(n, s)
            else:
                col = Sym(n, s)
            self.all.append(col)
            if s[-1] != 'X':
                if s[-1] == '!':
                    self.klass = col
                if s[-1] in ['+', '-']:
                    self.y.append(col)
                else:
                    self.x.append(col)