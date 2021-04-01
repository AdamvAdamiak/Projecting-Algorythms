import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import *
from scipy.spatial import distance


def x1(n):
    if n == 0:
        return 0
    return int((pow(3, n) + x1(n-1)))


def x2(n):
    if n == -1 or n == 0:
        return 0
    return int((n + x2(n-2)))


def x3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return int((x3(n-1) + x3(n-2)))

def ind_x1(n):
    return int(0.5*(2*0+3**(n+1)-3))

def ind_x2(n):
    if n%2 ==0:
        return int(n + (n/2)*(n/2 -1))
    else:
        return int(n + ((n-1)/2)**2)

def ind_x3(n):
    return int((((1+5**0.5)/2)**n / 5**0.5) - (((1-5**0.5)/2)**n / 5**0.5))

n = 5
for i in range(n):
    print('n = ',i)
    print(x1(i),ind_x1(i))
    print(x2(i),ind_x2(i))
    print(x3(i),ind_x3(i))


