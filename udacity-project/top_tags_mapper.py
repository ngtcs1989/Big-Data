
# coding: utf-8

# In[ ]:

#!/usr/bin/python
 
# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
# https://classroom.udacity.com/courses/ud617/lessons/717558831239847/concepts/24924385660923
 
import sys
import re
from collections import defaultdict
import csv
import re
tagdict = defaultdict(lambda: 0)
reader = csv.reader(sys.stdin,delimiter='\t')
for data in reader:
	qid,type,tagdata = data[0],data[5],data[2]
	if(qid == "id" or type!="question"):
		continue
	pattern = '[\S]+'
	tags = re.findall(pattern,tagdata)
	for tag in tags:
		tagdict[tag] += 1
for k,v in tagdict.iteritems():
	print k,v

