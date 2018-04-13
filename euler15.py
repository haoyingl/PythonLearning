#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler15.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Thu 01 Feb 2018 01:31:13 PM CST
#########################################################################
#!usr/bin/env python
cache={}
def f(x,y):
    if x==0 and y==0:
        cache[(x,y)]=0
    if x==0 or y==0:
        cache[(x,y)]=1
    if (x,y) not in cache:    
        cache[(x,y)]=f(x-1,y)+f(x,y-1)
    return cache[(x,y)]

print(f(20,20))



