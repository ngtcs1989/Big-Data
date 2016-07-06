
# coding: utf-8

# In[ ]:

#{
# 'areaCode': ['916'],
# 'areaLand': 109271000.0,
# 'country': 'United States',
# 'elevation': 13.716,
# 'foundingDate': datetime.datetime(2000, 7, 1, 0, 0),
# 'governmentType': ['Council\u2013manager government'],
# 'homepage': ['http://elkgrovecity.org/'],
# 'isPartOf': ['California', u'Sacramento County California'],
# 'lat': 38.4383,
# 'leaderTitle': 'Chief Of Police',
# 'lon': -121.382,
# 'motto': 'Proud Heritage Bright Future',
# 'name': 'City of Elk Grove',
# 'population': 155937,
# 'postalCode': '95624 95757 95758 95759',
# 'timeZone': ['Pacific Time Zone'],
# 'utcOffset': ['-7', '-8']
#}

#!/usr/bin/env python


from datetime import datetime
    
def range_query():
    # Modify the below line with your query.
    # You can use datetime(year, month, day) to specify date in the query
    query = {}
    query["foundingDate"] = {"$gte":datetime(2001,1,1),"$lt":datetime(2101,1,1)}
    return query

# Do not edit code below this line in the online code editor.
# Code here is for local use on your own computer.
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db

if __name__ == "__main__":
    # For local use
    db = get_db()
    query = range_query()
    cities = db.cities.find(query)

    print "Found cities:", cities.count()
    import pprint
    pprint.pprint(cities[0])


# In[ ]:

# Mongo DB update
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import csv
import json
import pprint

DATAFILE = 'arachnid.csv'
FIELDS ={'rdf-schema#label': 'label',
         'binomialAuthority_label': 'binomialAuthority'}


def add_field(filename, fields):
    """
    Complete this function to set up a dictionary for adding binomialAuthority
    information to the database.
    """
    process_fields = fields.keys()
    data = {}
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()
        # YOUR CODE HERE
        for line in reader:
            if line['binomialAuthority_label'] != 'NULL':
                data[line['rdf-schema#label'].split(' ')[0]] = line['binomialAuthority_label']
        #print data    
    return data


def update_db(data, db):
    """
    Use the dictionary you generated from add_field to update the database.
    """
    # YOUR CODE HERE
    for key in data:
        #res = db.arachnid.find_one({'label':key})
        res = db.arachnid.update({'label':key},{'$set':{'classification.binomialAuthority':data[key]}})
        

def test():
 
    
    data = add_field(DATAFILE, FIELDS)
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    update_db(data, db)

    updated = db.arachnid.find_one({'label': 'Opisthoncana'})
    assert updated['classification']['binomialAuthority'] == 'Embrik Strand'
    pprint.pprint(data)



if __name__ == "__main__":
    test()

