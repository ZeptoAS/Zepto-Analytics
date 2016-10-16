# -*- coding: utf-8 -*-
"""Public section, including homepage."""

from flask import (Blueprint, render_template, make_response, current_app, url_for, request)

blueprint = Blueprint('engine', __name__, static_folder="../static")


@blueprint.route("/profile")
def profile():
    return render_template("engine/profile.html")

