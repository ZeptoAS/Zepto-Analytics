"""
Power Data from Nordpoolspot

By Eirik Johannes Ramstad

"""

from __future__ import unicode_literals
import requests
from datetime import date, datetime, timedelta
from dateutil.parser import parse as parse_dt
from pytz import timezone, utc
from pprint import pprint

# Total Production Norway vs. Total Consumption Norway in MW

# Split down of production by source, hydro, coal, gas, wind osv. 

# API Power System Data -  i = Type + Area + Interval


API_URL = 'http://www.nordpoolspot.com/api/marketdata/page/%i'

# Request Type
PRODUCTION = 473 
CONSUMPTION = 586
EXCHANGE = 689
HYDRO_RESERVOIR = 736

# Area
ALL = 1
NORDIC = 7
BALTIC = 13
NO = 19
SE = 25
FI = 31
DK = 37
EE = 43
LT = 49
LV = 55

# Interval
HOURLY = 1
DAILY = 2
WEEKLY = 3
MONTHLY = 4
YEARLY = 5

def _parse_dt(time_str):
    ''' Parse datetimes to UTC from Stockholm time, which Nord Pool uses. '''
    time = parse_dt(time_str)
    return timezone('Europe/Stockholm').localize(time).astimezone(utc)


def fetch(reqtype, areas, interval):

    data_type = reqtype+areas+interval
    end_date = date.today() + timedelta(days=1)
    currency = "NOK"
    
    print(API_URL + str(data_type))

    r = requests.get(API_URL % data_type, params={
        'currency': currency,
        'endDate': end_date.strftime('%d-%m-%Y'),
        })
    

    json = r.json()
    data = json['data']
    
    finalData = []
    """
    for r in data['Rows']:
        startTime = r['StartTime']
        endTime = r['EndTime']
        for c in r['Columns']:
            name = c['Name']
            value = c['Value']
            item = dict(startTime=startTime, endTime=endTime, name=name, value=value)
            finalData.append(item)
    """
    names = []
    for r in data['Rows']:
        for c in r['Columns']:
            name = c['Name']
            if name not in names:
                names.append(name)

    length = len(names)
    
    names.pop(length-1)
    
    print(names)
    print(len(names))

    for x in range(len(names)):
        for r in data['Rows']:
            startTime = _parse_dt(r['StartTime'])
            endTime = _parse_dt(r['EndTime'])
            for c in r['Columns']:
                if names[x] == c['Name']:
                    name = c['Name']
                    value = c['Value']
                    strippedValue = value.replace(' ', '')
                    if value != "-" and value != ",":
                        item = dict(startTime=startTime, endTime=endTime, name=name, value=strippedValue)
                        finalData.append(item)

    return(finalData, names)




