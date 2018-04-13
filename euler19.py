#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler19.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Thu 08 Feb 2018 02:19:57 PM CST
#########################################################################
#!usr/bin/env python

LeapYearMonth=[31,29,31,30,31,30,31,31,30,31,30,31]
NotLeapYearMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
YearsOfMonth={}
for n in range(1900,2001):
    if n%4==0 and n%400!=0:
        YearsOfMonth[n]=LeapYearMonth
    else:
        YearsOfMonth[n]=NotLeapYearMonth

Begin=366
Sum=0
for n in range(1901,2001):
    for x in YearsOfMonth[n]:
        x+=Begin
        if x%7==0:
            Sum+=1
            Begin=0
        else:
            Begin=x%7

if x==35:
    Sum-=1

print(Sum)
