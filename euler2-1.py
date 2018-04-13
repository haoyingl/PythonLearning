#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler2-1.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Tue 09 Jan 2018 04:18:01 PM CST
#########################################################################
#!usr/bin/env python

a=0
b=1
c=counter=0

while True:
    c=a+b
    if c<4000000:
        a=b
        b=c
        if c%2==0:
            counter+=c
        else: continue
    else:break
print(counter)

