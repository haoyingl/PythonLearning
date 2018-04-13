#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler25.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Fri 02 Mar 2018 04:39:40 PM CST
#########################################################################
#!usr/bin/env python
a=1
b=1
c=a+b
count=3
strc=str(c)
while len(strc)!=1000:
    c=int(strc)
    a=b
    b=c
    c=a+b
    strc=str(c)
    count+=1

print(count)


