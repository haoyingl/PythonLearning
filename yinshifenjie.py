#-*- coding:utf-8 -*-
#########################################################################
# File Name: yinshifenjie.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Tue 30 Jan 2018 03:18:34 PM CST
#########################################################################
#!usr/b

m=22

suma=1/(m*(m+1))
while suma<=1/23:
    m+=1
    suma=suma+1/(m*(m+1))
    print(m,suma)
    continue
print (m,suma)
