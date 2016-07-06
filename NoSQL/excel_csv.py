
# coding: utf-8

# In[7]:


import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()

mapping = {'COAST':1,'EAST':2,'FAR_WEST':3,'NORTH':4,'NORTH_C':5,'SOUTHERN':6,'SOUTH_C':7,'WEST':8}
def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    #data = {'COAST':(0,0),'EAST':(0,0),'FAR_WEST':(0,0),'NORTH':(0,0),'NORTH_C':(0,0),'SOUTHERN':(0,0),'SOUTH_C':(0,0),'WEST':(0,0)}
    data = {}   
    for row in range(1,sheet.nrows):
        for elems in mapping:
            if elems not in data or data[elems][0] < sheet.cell_value(row,mapping[elems]):
                data[elems] = (sheet.cell_value(row,mapping[elems]),xlrd.xldate_as_tuple(sheet.cell_value(row,0),0))
          
    return data

def save_file(data, filename):
    writer = csv.writer(open(filename, 'wb'),delimiter='|')
    writer.writerow(['Station','Year','Month','Day','Hour','Max Load'])
    for k in mapping:
        dct = [k,data[k][1][0],data[k][1][1],data[k][1][2],data[k][1][3],data[k][0]]
        writer.writerow(dct)
    
      
def test():
    #open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)
    return

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)

        
if __name__ == "__main__":
    test()


# In[ ]:



