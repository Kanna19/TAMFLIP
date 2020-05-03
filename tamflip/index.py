from flask import g, render_template, request, url_for, Blueprint
from . import apiModule

bp = Blueprint('index', __name__, url_prefix="/")


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main.html')

    if request.method == 'POST':
        g.flightDetails = apiModule.getFlightDetails(request.form)
        print("Prothin")
        #print(g.flightDetails)
        return render_template('main.html')
