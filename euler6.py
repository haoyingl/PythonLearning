#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler6.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Thu 18 Jan 2018 10:56:58 AM CST
#########################################################################
#!usr/bin/env python
from math import *

def SumOfSquares(n):
    i = 0
    suma = 0
    while i<=n:
        suma+=pow(i,2)
        i+=1
    return suma

def SquaresOfSum(n):
    i = 0
    sumb = 0
    while i<=n:
        sumb+=i
        i+=1
    return pow(sumb,2)

print(SquaresOfSum(100),SumOfSquares(100),SquaresOfSum(100)-SumOfSquares(100))
