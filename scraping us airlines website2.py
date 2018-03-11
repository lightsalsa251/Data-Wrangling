import requests
from bs4 import BeautifulSoup
s = requests.Session()


#Session object is used so that any session object we get is maintained and used in the post reqeuest
r = s.get('http://www.transtats.bts.gov/Data_Elements.aspx?Data=2')
soup = BeautifulSoup(r.text)
ev = soup.find(id="__EVENTVALIDATION")
eventvalidation = ev["value"]
#finds the value of this id
vs = soup.find(id="__VIEWSTATE")
viewstate = vs["value"]
vsg = soup.find(id="__VIEWSTATEGENERATOR")
viewstategenerator = vsg["value"]

##r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
##                    data={'AirportList': "BOS",
##                          'CarrierList': "VX",
##                          'Submit': 'Submit',
##                          "__EVENTTARGET": "",
##                          "__EVENTARGUMENT": "",
##                          "__EVENTVALIDATION": eventvalidation,
##                          "__VIEWSTATE": viewstate
##                    })


r = s.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
           data = (
                   ("__EVENTTARGET", ""),
                   ("__EVENTARGUMENT", ""),
                   ("__VIEWSTATE", viewstate),
                   ("__VIEWSTATEGENERATOR",viewstategenerator),
                   ("__EVENTVALIDATION", eventvalidation),
                   ("CarrierList", "VX"),
                   ("AirportList", "BOS"),
                   ("Submit", "Submit")
                  ))

f = open('air.txt','w')
f.write(r.text)
