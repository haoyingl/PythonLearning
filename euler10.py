#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler10.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Mon 22 Jan 2018 04:39:11 PM CST
#########################################################################
#!usr/bin/env python
import base
Primes=[]
for n in range(9,2000000,2):
    if n%3==0 or n%5==0 or n%7==0:
        continue
    elif base.isPrime(n):
        Primes.append(n)
print(sum(Primes)+17)    

