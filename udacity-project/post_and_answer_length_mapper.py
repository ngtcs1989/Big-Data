
# coding: utf-8

# In[ ]:

#https://classroom.udacity.com/courses/ud617/lessons/717558831239847/concepts/25533285880923
import sys
import re
from collections import defaultdict
import csv
questions = defaultdict()
answers = defaultdict(list)
reader = csv.reader(sys.stdin,delimiter='\t')
for data in reader:
	qid, pid, type, body = data[0],data[6],data[5],data[4]
	if(qid == "id" or pid=="parent_id"):
		continue
    	#print id,type,len(body)
	if type == "question":
		questions[qid] = len(body)
	else:
		if pid not in answers:
			answers[pid].append(0)
			answers[pid].append(0)
		answers[pid][0] += len(body)
		answers[pid][1] += 1 
		#print id,answers[id][0],answers[id][1]
 
for k,v in questions.iteritems():
	print k,"Q",v
for k,v in answers.iteritems():
	print k,"A",v[0],v[1]

