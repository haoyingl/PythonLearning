#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler18.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Mon 05 Feb 2018 04:22:56 PM CST
#########################################################################
#!usr/bin/env python
file = open('maximumpath.txt')
Path={}
i=0
for line in file:
    parts=line.rstrip()
    L=parts.split()
    if L!=[]:
        Path[i]=L
        i+=1
    else: break
#print(Path)
i=13
while i>=0:
    ToMaxList=[]
    Num=len(Path[i])
    n=0
    while n<Num:
        New1=int(Path[i][n])+int(Path[i+1][n])
        New2=int(Path[i][n])+int(Path[i+1][n+1])
        ToMaxList.append(max(New1,New2))
        n+=1
    print(ToMaxList)

    Path[i]=ToMaxList
    i-=1

print(max(ToMaxList))


 
        



