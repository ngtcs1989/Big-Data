
# coding: utf-8

# In[ ]:

# https://classroom.udacity.com/courses/ud617/lessons/717558831239847/concepts/24924385660923
#!/usr/bin/python
 
import sys
from collections import defaultdict
 
cnt = 0
oldKey = None
 
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
tagdict = defaultdict(lambda: 0)
for line in sys.stdin:
    data_mapped = line.strip().split(" ")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
 
    thisKey, thisval = data_mapped
 
    if oldKey and oldKey != thisKey:
	tagdict[oldKey] += cnt 
	cnt =0
 
    oldKey = thisKey
    cnt += int(thisval)
 
if oldKey != None:
    tagdict[oldKey] += cnt 
 
cnt=1
for k,v in sorted(tagdict.iteritems(), key = lambda (k,v):(v,k), reverse=True):
	if cnt >10:
		break
	print k,v 
	cnt += 1

