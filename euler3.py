#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler3.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Tue 09 Jan 2018 04:44:21 PM CST
#########################################################################
#!usr/bin/env python

from math import * 
def Z(x):
    if x<2:
        return 1
    else:
        a = sqrt(x)
        i = 2 
        while i<=a:
            if x%i==0:
                return 0
                break
            else:
                i+=1
                continue
        return 1

def P(n):
        b = sqrt(n)
        t=1
        a=[]
        while t<b:
            if n%t==0:
                if Z(t)==1:
                    a.append(t)
                c = n/t
                if Z(c)==1:
                    return c
                else:
                    t+=1
                    continue
            else:
                t+=1
        tuple(a)
        return max(a)

print(P(600851475143))
