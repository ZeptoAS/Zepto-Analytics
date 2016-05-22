import json
import flask
import numpy as np

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("frontPage.html")

@app.route("/products")
def products():
    """
    A page for showing Zepto's products
    """
    return flask.render_template("products.html")

@app.route("/products/hub")
def productsHub():
    """
    A page for explaining the functionality of the Zepto Hub
    """
    return flask.render_template("hubInfo.html")

@app.route("/products/node")
def productsNode():
    """
    A page for explaining the functionality of the Zepto Nodes
    """
    return flask.render_template("nodeInfo.html")

@app.route("/products/engine")
def productsEngine():
    """
    A page for explaining the functionality of the Zepto Engine
    """
    return flask.render_template("engineInfo.html")

@app.route("/applications")
def applications():
    """
	A page about the different applications in which you can use the Zepto products!
    """
    return flask.render_template("applications.html")

@app.route("/contact")
def contact():
    """
	A contact us page!
    """
    return flask.render_template("contact.html")

    
@app.route("/company")
def company():
    """
    A page about Zepto as a company
    """
    return flask.render_template("company.html")

@app.route("/blog")
def blog():
    """
    The Zepto Blog
    """
    return flask.render_template("blog.html")

@app.route("/login")
def login():
    """
    A page for logging in to the Engine
    """
    return flask.render_template("login.html")

@app.route("/engine")
def engine():
    return flask.render_template("dashboard.html")

@app.route("/engine/analysis")
def analysis():
    """
    A page for doing analysing the data
    """
    return flask.render_template("analysis.html")
    
@app.route("/enigne/mynodes")
def mynodes():
    """
    A page for viewing my nodes
    """
    return flask.render_template("mynodes.html")

@app.route("/enigne/settings")
def settings():
    """
    A page for viewing and changing settings
    """
    return flask.render_template("mynodes.html")
    
@app.route("/enigne/logs")
def logs():
    """
    A page for viewing logs
    """
    return flask.render_template("mynodes.html")



@app.route("/api/data")
@app.route("/api/data/<int:ndata>")
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

@app.route("/api/data2")
@app.route("/api/data2/<int:ndata>")
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

if __name__ == "__main__":
    import os

    port = 80

    # Open a web browser pointing at the app.
    #os.system("open http://localhost:{0}".format(port))
   
    # Set up the development server on port 80.
    app.debug = True
    app.run(host='0.0.0.0', port=port, debug=True)