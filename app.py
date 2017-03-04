from flask import Flask, render_template

import public, engine, weather, nordpool

def register_blueprints(app):
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(engine.views.blueprint)
    app.register_blueprint(weather.views.blueprint)
    app.register_blueprint(nordpool.views.blueprint)

    return None

def register_extensions(app):
    return None

def register_errorhandlers(app):

    return None

app = Flask(__name__)
register_blueprints(app)


if __name__ == "__main__":

    # Start webserver
    app.debug = True
    app.run()
  


