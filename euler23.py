#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler23.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Sun 11 Feb 2018 01:44:41 PM CST
#########################################################################
#!usr/bin/env python
import base
AbundantNums={}
for n in range(2,28124):
    if n<base.SumOfProperDivisors(n):
        AbundantNums[n]=True
#print(AbundantNums)

total=0
for i in range(1,28124):
    for x in AbundantNums:
        if i<x:
            total+=i
            break
        elif AbundantNums.get(i-x):
            break
print(total)
""" 
TwoAbundantNums=[]
for x in AbundantNums:
    for y in AbundantNums:
        z=x+y
        if z>28123:
            break
        elif z in TwoAbundantNums:
            continue
        else:
            TwoAbundantNums.append(z)
total=0
for n in range(1,28124):
    if n not in TwoAbundantNums:
        total+=n
print(total)
"""
