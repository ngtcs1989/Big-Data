
# coding: utf-8

# In[ ]:

#!/usr/bin/python
# https://classroom.udacity.com/courses/ud617/lessons/717558831239847/concepts/25533285880923 
import sys
 
Qval = 0
Aval=0
Acount=0
oldKey = None
 
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
 
for line in sys.stdin:
    data_mapped = line.strip().split(" ")
    if len(data_mapped) != 3 and len(data_mapped) != 4:
        continue
    if len(data_mapped)==3:
    	thisKey, thisQval = int(data_mapped[0]), int(data_mapped[2])
    if len(data_mapped)==4:
    	thisKey, thisAval, thisAcount = int(data_mapped[0]), int(data_mapped[2]), int(data_mapped[3])
 
    if oldKey and oldKey != thisKey:
	if Qval != 0:
		if Aval != 0:
        		print oldKey, "\t", Qval, "\t",(Aval)/(1.0*Acount)
		else:
        		print oldKey, "\t", Qval, "\t",0
        oldKey = thisKey
        Acount = 0
	Aval=0
	Qval=0
 
    oldKey = thisKey
    if len(data_mapped) == 3:
    	Qval += thisQval	
    else:
	Aval += thisAval
	Acount += thisAcount			
 
if oldKey != None and Qval != 0:
	if Aval != 0:
        	print oldKey, "\t", Qval, "\t",(Aval)/(1.0*Acount)
	else:
        	print oldKey, "\t", Qval, "\t",0

