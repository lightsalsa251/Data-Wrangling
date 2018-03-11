#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format

"""

import xlrd
#from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


##def open_zip(datafile):
##    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
##        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    cv = sheet.col_values(1,start_rowx=1,end_rowx=None)
    s = sum(cv)
    s = s/float(len(cv))
    a = max(cv)
    b = min(cv)
    posa = cv.index(a)+1
    posb = cv.index(b)+1
    #1 is added because the list starts by the first row so to get the exact index of spreadsheet 1 is added

    
    e1 = sheet.cell_value(posa,0)
    e2 = sheet.cell_value(posb,0)
    e1 = xlrd.xldate_as_tuple(e1, 0)
    e2 = xlrd.xldate_as_tuple(e2, 0)
    data = {
            'maxtime': e1,
            'maxvalue': a,
            'mintime': e2,
            'minvalue': b,
            'avgcoast': s
    }
    return data


def test():
    #open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)
    #rounding is done so that there is no problem when there are many decimal places


test()
#pprint gets values printed in a structured manner
