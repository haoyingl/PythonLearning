#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler21.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Fri 09 Feb 2018 03:02:21 PM CST
#########################################################################
#!usr/bin/env python
import math
import base
def d(n):
    SqrN=math.sqrt(n)
    i=2
    Sum=1
    while i<=SqrN:
        if n%i==0:
            Sum+=i
            if n/i!=i:
                Sum+=n/i
        i+=1
    return Sum

AmicablePair=[]
for x in range(3,10001):
    Sum=0
    if base.isPrime(x):
        continue
    if x in AmicablePair:
        continue
    Sum=d(x)
    if Sum!=x and d(Sum)==x:
        AmicablePair.append(Sum)
        AmicablePair.append(x)
print(AmicablePair)
print(sum(AmicablePair))
 
