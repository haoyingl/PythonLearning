#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler9.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Mon 22 Jan 2018 11:06:27 AM CST
#########################################################################
#!usr/bin/env python
D={}
for n in range(1000):
    D[n]=n*n
a=1
while a<333:
    b=a+1
    while b<500:
        if D[a]+D[b]==D[1000-a-b]:
            product=a*b*(1000-a-b)
            print(a,b,1000-a-b)
            print(product)
            break
        else:
            b+=1
    a+=1

