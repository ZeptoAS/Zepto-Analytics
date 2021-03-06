# -*- coding: utf-8 -*-
"""Public section, including homepage."""

from flask import (Blueprint, render_template, make_response, current_app, url_for, request)
import configparser

blueprint = Blueprint('public', __name__, static_folder="../static")



@blueprint.route("/", methods=['GET', 'POST'])
def login():

    config = configparser.ConfigParser()
    config.read('config.cfg')

    email = config.get("profile", "email")
    password = config.get("profile", "password")

    if request.method == 'POST':

        inputemail = request.form['email']
        inputpassword = request.form['password']

        print(inputemail)

        if(email == inputemail and password == inputpassword):
            return render_template("public/dashboard.html")

    return render_template("public/login.html")


@blueprint.route("/dashboard")
def dashboard():
    return render_template("public/dashboard.html")

@blueprint.route("/settings")
def settings():
    
    config = configparser.ConfigParser()
    config.read('config.cfg')
    """
    config.add_section('Section1')
    config.set('Section1', 'an_int', '15')
    with open('example.cfg', 'wb') as configfile:
        config.write(configfile)
    """
    forecastiokey = config.get("forecastio", "apikey")
    
    templateData = {
    'forecastiokey': forecastiokey,
    }
    return render_template("public/settings.html", **templateData)	