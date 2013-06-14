#!/usr/bin/python

import re
import os


dirName=os.getcwd()
dirName+='/save'
dirs=os.listdir(dirName)
# prepare to remove the newest dir and the file of IP_port
dirs.sort()

#get domains
pattern = re.compile('http://.+?/')
domains = []
domainNew={}
domainDup={}

domainFile=open('domainFile1','w')
domainDupFile=open('domainDupFile1','w')
for dir in dirs[1:-1]:
	name=dirName+'/'+dir+'/index'	
	lines = open(name)
	for line in lines:
		domain=pattern.findall(line)[0]
		if domain in domainDup:
			domainDup[domain]+=1
		elif domain in domainNew:
			domainDup[domain]=1
		else:
			domainNew[domain]=1
			domainFile.write(domain+'\n')
domainFile.close()
sum=0
for item in domainDup:
	tmp= str(item)+' '+str(domainDup[item])
	domainDupFile.write(tmp+'\n')
	sum+=domainDup[item]
domainDupFile.write('Dup ip sum: '+str(sum)+'\n')
domainDupFile.close()
