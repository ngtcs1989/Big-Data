
# coding: utf-8

# In[ ]:

#!/usr/bin/python
# https://classroom.udacity.com/courses/ud617/lessons/713848763/concepts/7095786480923
import sys
 
salesTotal = 0.0
salesCount=0.0
oldKey = None
 
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
 
for line in sys.stdin:
    data_mapped = line.strip().split(" ")
    if len(data_mapped) != 3:
        continue
 
    thisKey, thisSale, thisCount = data_mapped
 
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", float(salesTotal)/float(salesCount)
        oldKey = thisKey;
        salesTotal = 0.0
 
    oldKey = thisKey
    salesTotal += float(thisSale)
    salesCount += float(thisCount) 
 
if oldKey != None:
    print oldKey, "\t", float(salesTotal)/float(salesCount)

