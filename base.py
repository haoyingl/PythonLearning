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

def SumOfProperDivisors(n):
    SqrN=sqrt(n)
    i=2
    Sum=1
    while i<=SqrN:
        if n%i==0:
            Sum+=i
            if n/i!=i:
                Sum+=n/i
        i+=1
    return Sum

def Fibonacci(n,cache=None):
    if cache == None:
        cache = {1:1,2:1}
    if n<3:
        return 1
    if n not in cache:
        cache[n] = Fibonacci(n-1,cache) + Fibonacci(n-2,cache)
    return cache[n]
