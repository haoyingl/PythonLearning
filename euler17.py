#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler17.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Fri 02 Feb 2018 03:53:05 PM CST
#########################################################################
#!usr/bin/env python
D={1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,'hundred':7,'thousand':8,'and':3}
suma=0
for n in range(1,100):
    if n in D:
        suma+=D[n]
    else:
        b=n%10
        c=n-b
        suma=suma+D[b]+D[c]
sumb=D[1]+D[2]+D[3]+D[4]+D[5]+D[6]+D[7]+D[8]+D[9]
sumc=D['and']*(900-9)+D['hundred']*900
sumtotal=suma*10+sumb*100+D[1]+D['thousand']+sumc

print(sumtotal)

