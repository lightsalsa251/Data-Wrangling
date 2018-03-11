from bs4 import BeautifulSoup
def options(soup,id):
    option_values = []
    carrier_list = soup.find(id=id)
    #html id of carriers is CarrierList
    for option in carrier_list.find_all('option'):#find all descendents of the options tag
        option_values.append(option['value'])
    return option_values

def print_list(label,codes):
    print('\n',label)
    for c in codes:
        print(c)

#def main():
soup = BeautifulSoup(open('Data_Elements.htm'))

codes = options(soup,'CarrierList')
print_list('Carriers',codes)

codes = options(soup,'AirportList')
print_list('Airports',codes)

#we have to look it at the forms tag to see how to get the data as it will define the request to be made
#in order to mine the data we need, we have to figure out how we programmatically construct requests in order to pull each paage of data we need
#to do this we can see how the browser makes requests
#look at the netwkork tab
#to get the details submit the request again, if an error is thrown open the page again in a new tab
#simply reloading won't work
#in form data tag we will find that there is more work to do
#_VIEWSTATEGENERATOR may also be needed to be passed along with other form data depending on the browser
#all form elements may not be the part of the user interface/form
#these form elements will be hidden
#locate these, these will be present somewhere in the tags after the form tag
#these form parameters validates each request that comes in
#airport and carrier values have been hardcoded below, actually we will loop through all possible combinations of the two codes lists formed above


#getting the form parameters
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the appropriate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function

from bs4 import BeautifulSoup
import requests
import json

html_page = "page_source.html"


def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
     with open(page, "r") as html:
        soup = BeautifulSoup(html, "lxml")
        ev = soup.find(id="__EVENTVALIDATION")
        data["eventvalidation"] = ev["value"]
        #finds the value of this id
        vs = soup.find(id="__VIEWSTATE")
        data["viewstate"] = vs["value"]

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
##Note that the second argument to the BeautifulSoup function, "lxml", comes from the parser in the Python library 'lxml'. Other parsers can be set up as the second argument, such as the Python library's default "html.parser" or other options as shown in the documentation.
##Take note of this argument when working with BeautifulSoup on your local computer.
