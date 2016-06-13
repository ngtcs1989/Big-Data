
# coding: utf-8

# In[ ]:

#!/usr/bin/python
 
# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
# https://classroom.udacity.com/courses/ud617/lessons/713848763/concepts/7095786480923
 
import sys
from datetime import datetime
dct= {0:[0.0,0],1:[0.0,0],2:[0.0,0],3:[0.0,0],4:[0.0,0],5:[0.0,0],6:[0.0,0]}
for line in sys.stdin:
	data = line.strip().split('\t')
	date, sales = data[0],data[4]
	day = datetime.strptime(date,"%Y-%m-%d").weekday()	
	dct[day][0] += float(sales)
	dct[day][1] += 1
for k in dct:
	print k, dct[k][0], dct[k][1]

