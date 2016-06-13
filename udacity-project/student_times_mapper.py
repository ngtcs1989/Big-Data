
# coding: utf-8

# In[ ]:

#!/usr/bin/python
 
# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
# https://classroom.udacity.com/courses/ud617/lessons/717558831239847/concepts/7302987470923
 
import sys
import re
from collections import defaultdict
import csv
dct = defaultdict(list)
reader = csv.reader(sys.stdin,delimiter='\t')
for data in reader:
	id, date = data[3],data[8]
	if(id=="author_id"):
		continue
    	pattern = '(?P<Y>\S+)-(?P<O>\S+)-(?P<D>\S+)\s+(?P<H>\S+):(?P<M>\S+):(?P<S>\S+)\S+'
    	res = re.match(pattern,date)
    	print id,date,res.group('H')
	dct[int(id)].append(res.group('H'))
 
for k,v in dct.iteritems():
	for i in v:
		print k,i

