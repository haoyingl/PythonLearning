#-*- coding:utf-8 -*-
#########################################################################
# File Name: euler10_2.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Tue 23 Jan 2018 02:00:24 PM CST
#########################################################################
#!usr/bin/env python
D={}
for n in range(2, 20):
    D[n]=True
Sequence = list(D.keys())
i =0
while i<18:
    if D[Sequence[i]]:
        print ("Sequence[i={}]={}".format(i,Sequence[i]))
        j=i+1
        #while j< 18 :
        while j<18 and D[Sequence[j]]:
            if Sequence[j]%Sequence[i]==0:
                D[Sequence[j]] = False
            print("Sequence[j={}]={} {}".format(j, Sequence[j], D[Sequence[j]]))
            j+=1
    i+=1
print(D)
SequencePrime=[]
for keys in D:
    if D[keys]:
        SequencePrime.append(keys)
print(sum(SequencePrime))
