#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler16.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Fri 02 Feb 2018 02:54:02 PM CST
#########################################################################
#!usr/bin/env python
A=2**1000
B=str(A)
L=[]
i=0
while i<len(B):
    C=int(B[i])
    L.append(C)
    i+=1
print(sum(L))
