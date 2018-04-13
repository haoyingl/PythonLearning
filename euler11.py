#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler11.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Fri 26 Jan 2018 03:14:28 PM CST
#########################################################################
#!usr/bin/env python
i=0
DiagonalLine={}


for line in open('diagonal_line.txt'):
    DiagonalLine[i]=line.split()
    i+=1

AllProduct=[]
List = list(DiagonalLine.keys())
Maxkey=max(List)
print(Maxkey)
print(len(DiagonalLine[1]))
#print(DiagonalLine[20][2])

k=0
while k<Maxkey-2:
    j=0
    while j<len(DiagonalLine[k])-3:
        product1=int(DiagonalLine[k][j])*int(DiagonalLine[k+1][j+1])*int(DiagonalLine[k+2][j+2])*int(DiagonalLine[k+3][j+3])
        #product=int(a)*int(b)*int(c)*int(d)
        AllProduct.append(product1)
        j+=1
    k+=1
    
k=0
while k<=Maxkey:
    j=0
    while j<len(DiagonalLine[k])-3:
        product2=int(DiagonalLine[k][j])*int(DiagonalLine[k][j+1])*int(DiagonalLine[k][j+2])*int(DiagonalLine[k][j+3])
        AllProduct.append(product2)
        j+=1
    k+=1

k=Maxkey
while k>2:
    j=len(DiagonalLine[k])-4
    while j>=0:
        product4=int(DiagonalLine[k][j])*int(DiagonalLine[k-1][j+1])*int(DiagonalLine[k-2][j+2])*int(DiagonalLine[k-3][j+3])
        AllProduct.append(product4)
        j-=1
    k-=1

k=0
while k<Maxkey-2:
    j=len(DiagonalLine[k])-1
    while j>=0:
        product3=int(DiagonalLine[k][j])*int(DiagonalLine[k+1][j])*int(DiagonalLine[k+2][j])*int(DiagonalLine[k+3][j])
        AllProduct.append(product3)
        j-=1
    k+=1
print(max(AllProduct))

