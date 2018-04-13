#-*- coding:utf-8 -*-
#########################################################################
# File Name: bigproject.py
# Author: Liang Haoying
# mail: Haoying.Liang@nokia-sbell.com
# Created Time: Tue 03 Apr 2018 02:41:16 PM CST
#########################################################################
#!usr/bin/env python
trace=open('/tmp/svn.log')
Table={}
for line in trace:
	if line[0]=='r':
		data=line.split('|')[0:-1]
		Table['index']=data[0]
		Table['name']=data[1]
		Table['time']=data[2]
		trace.readline()
		files = trace.readline()
		files = files.replace(' ','').rstrip()
		filename=[]
		while files.startswith('M') or files.startswith('A'):
			TempFile = files.split('/')
			filename.append(TempFile[-1])
			files = trace.readline()
			files = files.replace(' ','').rstrip()
		Table['FileName']=filename
		Table['comments']=trace.readline().rstrip()
		print(Table)
