# -*- coding: utf-8 -*-
"""Public section, including homepage."""

from flask import (Blueprint, render_template, make_response, current_app, url_for, request)


blueprint = Blueprint('public', __name__, static_folder="../static")


@blueprint.route("/")
def index():
    return render_template("public/frontPage.html")

@blueprint.route("/products")
def products():
    """
    A page for showing Zepto's products
    """
    return render_template("public/products.html")

@blueprint.route("/products/hub")
def productsHub():
    """
    A page for explaining the functionality of the Zepto Hub
    """
    return render_template("public/hubInfo.html")

@blueprint.route("/products/node")
def productsNode():
    """
    A page for explaining the functionality of the Zepto Nodes
    """
    return render_template("public/nodeInfo.html")

@blueprint.route("/products/engine")
def productsEngine():
    """
    A page for explaining the functionality of the Zepto Engine
    """
    return render_template("public/engineInfo.html")

@blueprint.route("/applications")
def applications():
    """
    A page about the different applications in which you can use the Zepto products!
    """
    return render_template("public/applications.html")

@blueprint.route("/contact")
def contact():
    """
    A contact us page!
    """
    return render_template("public/contact.html")

    
@blueprint.route("/company")
def company():
    """
    A page about Zepto as a company
    """
    return render_template("public/company.html")

@blueprint.route("/blog")
def blog():
    """
    The Zepto Blog
    """
    return render_template("public/blog.html")

@blueprint.route("/login")
def login():
    """
    A page for logging in to the Engine
    """
    return render_template("public/login.html")