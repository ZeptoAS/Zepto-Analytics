
import json
from flask import Flask, render_template
import numpy as np

import public, engine


def register_blueprints(app):
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(engine.views.blueprint)
    return None




def register_extensions(app):

    return None


def register_errorhandlers(app):

    return None


#def create_app(config_object=ProdConfig):

app = Flask(__name__)
#app.config.from_object(config_object)
#register_extensions(app)
register_blueprints(app)
#register_errorhandlers(app)

#    return app


if __name__ == "__main__":
    import os

    port = 80

    # Open a web browser pointing at the app.
    #os.system("open http://localhost:{0}".format(port))
   
    # Set up the development server on port 80.

    app.debug = True
    app.run(host='0.0.0.0', port=port, debug=True)

    