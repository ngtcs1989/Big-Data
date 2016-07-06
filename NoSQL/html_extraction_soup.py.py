
# coding: utf-8

# In[ ]:

#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import json

html_page = "page_source.html"



def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html,"lxml")
        inputTag1 = soup.findAll(attrs={"id" : "__EVENTVALIDATION"})
        inputTag2 = soup.findAll(attrs={"id" : "__VIEWSTATE"})
        for i in inputTag1:
            data["eventvalidation"] = i['value']
        for i in inputTag2:
            data["viewstate"] = i['value']    
        # Alternatively
        #inputTag1 = soup.find(attrs={"id" : "__EVENTVALIDATION"})
        #inputTag2 = soup.find(attrs={"id" : "__VIEWSTATE"})
        #data["eventvalidation"] = inputTag1['value']
        #data["viewstate"] = inputTag2['value']    
        #print inputTag1
        pass

    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text


def test():
    data = extract_data(html_page)
    assert data["eventvalidation"] != ""
    assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
    assert data["viewstate"].startswith("/wEPDwUKLTI")

    
test()


# In[ ]:

#!/usr/bin/env python


from bs4 import BeautifulSoup
html_page = "options.html"


def extract_carriers(page):
    data = []

    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        tags = soup.find_all('select',attrs={"id":"CarrierList"})
        for i in tags:
            res = i.find_all('option');
            for j in res:
                if j['value'][:3] != "All":
                    data.append(j['value'])
                    # j.text for value between tags
    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airport = data["airport"]
    carrier = data["carrier"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': airport,
                          'CarrierList': carrier,
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text


def test():
    data = extract_carriers(html_page)
    assert len(data) == 16
    assert "FL" in data
    assert "NK" in data

test()

