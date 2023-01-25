import sys

import TestEngine
from Sym import Sym
from Num import Num
from Data import Data
from Utils import rnd,csv,rand
tot=0
def count(t):
    global tot
    tot = tot + len(t)

def eg_check_syms(the):
    sym = Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    assert 'a' == sym.mid() and 1.379 == rnd(sym.div())


def eg_check_nums(the):
    num = Num()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    assert 11 / 7 == num.mid() and 0.787 == rnd(num.div())


def eg_the(the):
    print(the)
    pass

def eg_check_rands(the):
    num1=Num()
    num2=Num()
    Seed=the['seed']
    for i in (1,1001):
        x,Seed = rand(0,1,Seed)
        num1.add(x)
    Seed=the['seed']
    for i in (1,1001):
        x,Seed = rand(0,1,Seed)
        num2.add(x)
    m1=rnd(num1.mid(),10)
    m2=rnd(num2.mid(),10)
    assert m1==m2 and .5==rnd(m1,1)

def eg_csv(the):
    csv(the['file'],count)
    assert tot == 8*399

def eg_data(the):
    data = Data(the['file'])
    assert len(data.rows) == 398 and \
            data.cols.y[0].w == -1 and \
            data.cols.x[0].at == 0 and \
            len(data.cols.x)==4


def eg_stats(the):
    data=Data(the['file'])
    temp={}
    temp.update({"y":data.cols.y,"x":data.cols.x})
    for k,cols in temp.items():
        print(k,"mid",data.stats(cols,2,"mid"))
        print("", "div",data.stats(cols,2,"div"))
    