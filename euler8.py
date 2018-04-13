#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler8.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Thu 18 Jan 2018 02:31:53 PM CST
#########################################################################
#!usr/bin/env python
myfile = open(r'adjacentdigits.txt')
aString=myfile.read()
bString=aString.replace('\n','')
aList= list(bString)
ProductList=[]
for i in range(0,987):
    bList = aList[i:i+13]
    product = 1
    if '0' in bList:
        continue
    else:
        for x in bList:
            product*=(int)(x)
    ProductList.append(product)
MaxProduct=max(ProductList)
print(MaxProduct)


