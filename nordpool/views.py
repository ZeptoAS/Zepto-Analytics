# -*- coding: utf-8 -*-
"""Nordpool section"""

from flask import (Blueprint, render_template, make_response, current_app, url_for, request, jsonify)
import configparser
import datetime
from nordpool.nordpool import *

blueprint = Blueprint('nordpool', __name__, static_folder="../static")


config = configparser.ConfigParser()
config.read('config.cfg')

#apikey = config.get("nordpool", "apikey")

reqtype1 = PRODUCTION
reqtype2 = CONSUMPTION
areas = NORDIC
interval = MONTHLY

@blueprint.route("/nordpool", methods=['GET', 'POST'])
def index():

    global areas
    global interval
    
    if request.method == "POST":        
        areas = request.form[areas]
        interval = request.form[interval]
    
    data = fetch(reqtype1, areas, interval)
    consumptiondata = fetch(reqtype2, areas, interval)

    print(data[1])
    templateData = {
    'data': data[0],
    'names': data[1],
    'condata': consumptiondata[0],
    'connames': consumptiondata[1],
    }

    return render_template("nordpool/main.html", **templateData)	
