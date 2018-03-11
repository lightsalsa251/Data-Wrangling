import csv
import pprint

DATAFILE = 'beatles-discography.csv'

def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile) as sd:
        r = csv.DictReader(sd)
        # r is a list of dictionaries
        for line in r:
            data.append(line)
    return data

d = parse_csv(DATAFILE)
# d is a list of tupples of list of tuples
##pprint.pprint(d['Title'])
for i in d:
    print(i['Title'])

# In python 3.6 DictReader returns ordered dicts which can be added to a list and it can be iterated as above

