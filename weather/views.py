# -*- coding: utf-8 -*-
"""Weather section"""

from flask import (Blueprint, render_template, make_response, current_app, url_for, request, jsonify)
import configparser
import datetime
from pprint import pprint

blueprint = Blueprint('weather', __name__, static_folder="../static")

from forecastiopy import *

config = configparser.ConfigParser()
config.read('config.cfg')

apikey = config.get("forecastio", "apikey")

Stavanger = [58.97005, 5.73332, "Stavanger"]


@blueprint.route("/weather")
def index():
    
    city = Stavanger
    
    fio = ForecastIO.ForecastIO(apikey,
                                units=ForecastIO.ForecastIO.UNITS_SI,
                                lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                                latitude=city[0], longitude=city[1])

    current = get_currently(fio)
    hourly = get_hourly_temp(fio)
    #pprint(hourly)
    templateData = {
    'city': city[2],
    'current': current,
    #'minutely': minutely,
    'hourly': hourly,
    #'daily': daily
    }
    return render_template("weather/weather.html", **templateData)	

def get_currently(fio):
    
    if fio.has_currently() is True:
        currently = FIOCurrently.FIOCurrently(fio)
        """
        print 'Currently'
        for item in currently.get().keys():
            print item + ' : ' + unicode(currently.get()[item])
        print
        # Or access attributes directly
        print currently.temperature
        print currently.humidity
        print
        """
        return currently
    else:
        print('No Currently data')



def get_minutely(fio):
	
    if fio.has_minutely() is True:
        minutely = FIOMinutely.FIOMinutely(fio)
        """
        print 'Minutely'
        print 'Summary:', minutely.summary
        print 'Icon:', minutely.icon
        print
        for minute in xrange(0, minutely.minutes()):
            print 'Minute', minute+1
            for item in minutely.get_minute(minute).keys():
                print item + ' : ' + unicode(minutely.get_minute(minute)[item])
            print
            # Or access attributes directly for a given minute. 
            # minutely.minute_3_time would also work
            print minutely.minute_1_time
            print
        print
        """
        return minutely
    else:
        print('No Minutely data')

def get_hourly(fio):

	if fio.has_hourly() is True:
	    hourly = FIOHourly.FIOHourly(fio)
	    """
	    print 'Hourly'
	    print 'Summary:', hourly.summary
	    print 'Icon:', hourly.icon
	    print
	    for hour in xrange(0, hourly.hours()):
	        print 'Hour', hour+1
	        for item in hourly.get_hour(hour).keys():
	            print item + ' : ' + unicode(hourly.get_hour(hour)[item])
	        print
	        # Or access attributes directly for a given minute. 
	        # hourly.hour_5_time would also work
	        print hourly.hour_3_time
	        print
	    print
	    """
	    return hourly
	else:
	    print('No Hourly data')

def get_daily(fio):

	if fio.has_daily() is True:
	    daily = FIODaily.FIODaily(fio)
	    """
	    print 'Daily'
	    print 'Summary:', daily.summary
	    print 'Icon:', daily.icon
	    print
	    for day in xrange(0, daily.days()):
	        print 'Day', day+1
	        for item in daily.get_day(day).keys():
	            print item + ' : ' + unicode(daily.get_day(day)[item])
	        print
	        # Or access attributes directly for a given minute. 
	        # daily.day_7_time would also work
	        print daily.day_5_time
	        print
	    print
	    """
	    return daily
	else:
	    print('No Daily data')

def get_flags(fio):

	if fio.has_flags() is True:
	    from pprint import pprint
	    flags = FIOFlags.FIOFlags(fio)
	    pprint(vars(flags))
	    # Get units directly
	    print(flags.units)
	else:
	    print('No Flags data')

def get_hourly_temp(fio): 
    data = []
    if fio.has_hourly() is True:
        hourly = FIOHourly.FIOHourly(fio)
        for hour in range(0, hourly.hours()):
            for item in hourly.get_hour(hour).keys():
                if item == "temperature":
                    temperature = hourly.get_hour(hour)[item]
                if item == "humidity":
                    humidity = hourly.get_hour(hour)[item]
                if item == "pressure":
                    pressure = hourly.get_hour(hour)[item]
                if item == "windSpeed":
                    windspeed = hourly.get_hour(hour)[item]
                if item == "precipIntensity":
                    precipIntensity = hourly.get_hour(hour)[item]
                if item == "time":
                    time = get_time(hourly.get_hour(hour)[item])
            item = dict(time=time, temperature=temperature, humidity=humidity, pressure=pressure, windspeed=windspeed, precipIntensity=precipIntensity)
            data.append(item)
        #print data
    else:
        print('No Hourly data')
    return data

def get_time(unix_time):
    time = datetime.datetime.fromtimestamp(int(unix_time))
    #.strftime('%Y-%m-%d %H:%M:%S'))
    return time
