#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler12.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Mon 29 Jan 2018 05:30:40 PM CST
#########################################################################
#!usr/bin/env python
from math import *

def T(n):
    return n*(n+1)/2

for n in range(1,100000):
    a = T(n)
    b = sqrt(a)
    j = 1
    k = 0
    flag = False
    while j<=b:
        if a%j==0:
            k+=2
            if k==500:
                print(a)
                flag = True
                break
        j+=1
    if flag:
        break

    
