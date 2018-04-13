#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler7.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Thu 18 Jan 2018 02:10:32 PM CST
#########################################################################
#!usr/bin/env python
import base

n=2
count = 1
while count<10002:
    if base.isPrime(n):
        count+=1
    n+=1
n=n-1
print(n)

