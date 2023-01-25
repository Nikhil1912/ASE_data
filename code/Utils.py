import math
from Main import coerce
import os

def rnd(n, nPlaces=3):
    mult = pow(10, nPlaces)
    return math.floor(n * mult + 0.5) / mult

def rand(lo=0,hi=1,Seed=937162211):
    #Seed=937162211
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647,Seed

def rint(lo,hi):
    return math.floor(0.5 + rand(lo,hi))

def csv(src,fun):
    if not os.path.isfile(src):
        print("\nfile "+src+" doesn't exists!")
        sys.exit(2)
    with open(src, 'r') as file1:
        for line in file1:
            temp=[]
            for j in line.strip().split(','):
                temp.append(coerce(j))
            fun(temp)

def map(src,fun):
    for i in src:
        fun(i)

def kap(t,fun, u={}):
    u={}
    for k,v in enumerate(t):
        v,k=fun(k,v)
        if not k:
            u[len(u)]=v
        else:
            u[k]=v
    return u



