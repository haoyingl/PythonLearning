#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler14.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Wed 31 Jan 2018 10:19:49 AM CST
#########################################################################
#!usr/bin/env python
def IterativeSeq(n):
    if n%2==0:
        n=n/2
    else:
        n=n*3+1
    return n
D={}
d={}
for t in range(1000000,1,-1):
    Terms=1
    keys=[]
    while t>1:
        if t in D:
            vals=list(range(Terms+D[t]-1,D[t],-1))
            break
        keys.append(t)
        t=IterativeSeq(t)
        Terms+=1
    if t==1:
        vals=list(range(Terms,1,-1))
    #print(keys,vals)
    d = dict(zip(keys,vals))
    #print(d)
    D.update(d)
ChainList=list(D.values())
M=max(ChainList)
for key in D:
    if D[key]==M:
        print(key,D[key])
