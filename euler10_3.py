#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler10_2.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Tue 23 Jan 2018 02:00:24 PM CST
#########################################################################
#!usr/bin/env python
maxThreshold = 2000000
D={}
for n in range(2, maxThreshold):
    D[n]=True

for n in range(2, maxThreshold):
    if not D[n] :
        continue

    for m in range(2, maxThreshold) :
        if n * m > maxThreshold :
            break
        D[n*m] = False

sum=0
for n in range(2, maxThreshold):
    if D[n] :
        sum += n;
print(sum)

