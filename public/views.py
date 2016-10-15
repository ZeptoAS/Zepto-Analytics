# -*- coding: utf-8 -*-
"""Public section, including homepage."""

from flask import (Blueprint, render_template, make_response, current_app, url_for, request)


blueprint = Blueprint('public', __name__, static_folder="../static")


@blueprint.route("/")
def login():
    return render_template("public/login.html")
