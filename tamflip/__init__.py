#Application Factory
import os
from flask import Flask
from flask import render_template
from flask import request, g
from . import apiModule

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'tamflip.sqlite'),
    )

    #ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Link with Database
    from . import db
    db.init_app(app)

    #Link blueprints
    from . import index
    app.register_blueprint(index.bp)

    return app
