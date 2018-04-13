#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler13.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Tue 30 Jan 2018 08:47:47 PM CST
#########################################################################
#!usr/bin/env python
Sum = 0
for line in open('100digit.txt'):
    a = int(line)
    Sum +=a
print(Sum)
