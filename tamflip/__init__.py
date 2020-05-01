#Application Factory
import os
from flask import Flask
from flask import render_template
from flask import request

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

    # istart page
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            return render_template('main.html')

        if request.method == 'POST':
            # return render_template('main.html', submitted=True)
            res = "Form Submitted<br>"
            res += request.form.get('fromLocation')
            return res


    return app
