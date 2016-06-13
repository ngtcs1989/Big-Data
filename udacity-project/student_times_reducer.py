
# coding: utf-8

# In[ ]:

#!/usr/bin/python
# https://classroom.udacity.com/courses/ud617/lessons/717558831239847/concepts/7302987470923 
import sys
 
 
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
 
for line in sys.stdin:
    data_mapped = line.strip().split(" ")
    if len(data_mapped) != 2:
        continue
 
    print data_mapped[0],data_mapped[1]

