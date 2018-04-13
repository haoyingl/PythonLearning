#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler24.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Sun 11 Feb 2018 04:29:14 PM CST
#########################################################################
#!usr/bin/env python
'''
LexicographicOrder=[]
for n in range(123456789,9876543211):
    s=str(n)
    if len(s)==9 and '9'in s and '8'in s and '7'in s and '6'in s and '5'in s and '4'in s and '3'in s and '2'in s and '1' in s:
        s='0'+s
        n=int(s)
        LexicographicOrder.append(n)
    elif '9'in s and '8'in s and '7'in s and '6'in s and '5'in s and '4'in s and '3'in s and '2'in s and '1'in s and '0'in s:
        n=int(s)
        LexicographicOrder.append(n)
print(LexicographicOrder[999999])
'''

from math import *
init='0123456789'
s=''
num=999999  
#if u wants the 10000th lexicographicorder number, then the num here should be 10000-1=9999
length=len(init)-1
while num>0:
    divided=num//factorial(length)
    num=num%factorial(length)    
    s=s+init[divided]
    init=init[0:divided]+init[divided+1:] 
    length-=1

s=s+init
   
print(int(s))
    



