#-*- coding:utf-8 -*-
#########################################################################
# File Name: test.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Tue 09 Jan 2018 02:02:20 PM CST
#########################################################################
#!usr/bin/env python

def F(n,cache=None):
    if cache == None:
        cache = {1:1}
    if n<2:
        return 1
    if n not in cache:
#        print(cache,n)
        cache[n] = F(n-1,cache) + F(n-2,cache)
#        print (cache,n)
    return cache[n]

f = []
for n in range(2000000):
    if F(n)>4000000:
        break
    elif F(n)%2==0:
        f.append(F(n))

print(sum(f))
    

