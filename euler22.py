#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler22.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Fri 09 Feb 2018 04:28:13 PM CST
#########################################################################
#!usr/bin/env python
NameFile=open("names.txt")
Namestr=NameFile.read()
Namelst=Namestr.split(',')
Namelst.sort()
def StrInvertToAlphabetialOrder(S):
    Sum=0
    for x in S:
        if 64<ord(x)<91:
            Sum+=(ord(x)-64)
        elif 96<ord(x)<123:
            Sum+=(ord(x)-96)
    return Sum

NameDic={}
i=1
for name in Namelst:
    NameDic[i]=StrInvertToAlphabetialOrder(name)    
    i+=1
#print(NameDic)
i=1
Sum=0
while i in NameDic:
    Sum+=(i*NameDic[i])
    i+=1


print(Sum)
