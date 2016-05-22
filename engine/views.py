# -*- coding: utf-8 -*-
"""Engine section"""

from flask import (Blueprint, render_template, make_response, current_app, url_for, request)


blueprint = Blueprint('engine', __name__, static_folder="../static")


@blueprint.route("/engine")
def engine():
    return render_template("engine/dashboard.html")

@blueprint.route("/engine/analysis")
def analysis():
    """
    A page for doing analysing the data
    """
    return render_template("engine/analysis.html")
    
@blueprint.route("/engine/mynodes")
def mynodes():
    """
    A page for viewing my nodes
    """
    return render_template("engine/mynodes.html")

@blueprint.route("/enigne/settings")
def settings():
    """
    A page for viewing and changing settings
    """
    return render_template("engine/mynodes.html")
    
@blueprint.route("/enigne/logs")
def logs():
    """
    A page for viewing logs
    """
    return render_template("engine/mynodes.html")



@blueprint.route("/api/data")
@blueprint.route("/api/data/<int:ndata>")
def data(ndata=100):
    """ 
    On request, this returns a list of ``ndata`` randomly made data points.
    :param ndata: (optional)
        The number of data points to return.
    :returns data:
        A JSON string of ``ndata`` data points.
    """ 
    x = 10 * np.random.rand(ndata) - 5
    y = 0.5 * x + 0.5 * np.random.randn(ndata)

    return json.dumps([{"x": i, "y": y[i]}
        for i in range(ndata)])

@blueprint.route("/api/data2")
@blueprint.route("/api/data2/<int:ndata>")
def data2(ndata=100):
    """ 
    On request, this returns a list of ``ndata`` randomly made data points.
    :param ndata: (optional)
        The number of data points to return.
    :returns data:
        A JSON string of ``ndata`` data points.
    """ 
    
    #x = 
    y = 20 * np.random.randn(ndata)

    return json.dumps([{"x": i/10, "y": y[i]}
        for i in range(ndata)])
