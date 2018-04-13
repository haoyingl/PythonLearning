#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler5.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Tue 16 Jan 2018 10:36:50 AM CST
#########################################################################
#!usr/bin/env python

from math import *

def isPrime(n):
    if n<2:
        return True
    else:
        sqrt_n = sqrt(n)
        i = 2
        while i<=sqrt_n:
            if n%i==0:
                return False
                break
            else:
                i+=1
                continue
        return True

def GreatestCommonDivisor(a,b):
    while(b%a!=0):
        c = b%a
        b = a
        a = c
    GreatestCommonDivisor=a    
         
    return GreatestCommonDivisor

def LeastCommonMutiple(a,b):
    product = a*b
    LeastCommonMutiple = a*b/GreatestCommonDivisor(a,b)
    return LeastCommonMutiple

product =1
for i in range(1,21):    
    if isPrime(i):
        product *=i
    else:
        product = LeastCommonMutiple(product,i)
    i+=1

print(product)
    

