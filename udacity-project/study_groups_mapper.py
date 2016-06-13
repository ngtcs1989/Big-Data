
# coding: utf-8

# In[ ]:

#!/usr/bin/python
 
# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
# https://classroom.udacity.com/courses/ud617/lessons/717558831239847/concepts/25478286080923
 
import sys
import re
from collections import defaultdict
import csv
post = defaultdict(list)
reader = csv.reader(sys.stdin,delimiter='\t')
for data in reader:
	qid, sid, type, pid = data[0],data[3],data[5],data[6]
	if(qid == "id"):
		continue
    	#print id,type,len(body)
	if type == "question":
		post[qid].append(sid)
	else:
		post[pid].append(sid)
 
 
for k,v in post.iteritems():
	print k,"\t",v

