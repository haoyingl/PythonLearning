#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler4.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Thu 11 Jan 2018 10:56:04 AM CST
#########################################################################
#!usr/bin/env python

palind=[]
for n in range(10000,999*999):
    s = str(n)
    if (s[0]==s[-1])&(s[1]==s[-2])&(s[2]==s[-3]):
            palind.append(int(s))
            continue
    continue

palind.reverse()

D={}
for x in palind:
    for i in range(100,999):
        if (x%i==0)&(x/i<1000):
            D[i]=x
            print(x,"=",i,"*",x/i)
            break
        continue
    if D=={}:
        continue
    else:
        break





