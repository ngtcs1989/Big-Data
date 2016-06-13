
# coding: utf-8

# In[ ]:

# https://classroom.udacity.com/courses/ud617/lessons/717558831239847/concepts/25478286080923
#!/usr/bin/python
 
import sys
from collections import defaultdict
import re
 
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
oldkey = None
cur = list()
postdict = defaultdict(list)
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    #print data_mapped[0],"###",data_mapped[1]
    curkey = data_mapped[0]
    pattern ='[\d]+'
    sids = re.findall(pattern,data_mapped[1])
    if oldkey and oldkey!=curkey:
	print oldkey, cur
	cur = list()	
    oldkey = curkey
    for k in sids:
    	cur.append(k)
 
if oldkey:
	print oldkey, cur

