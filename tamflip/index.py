from flask import g, render_template, request, url_for, Blueprint
from . import api_module

bp = Blueprint('index', __name__, url_prefix="/")


@bp.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('main.html')

	if request.method == 'POST':
		(flight_details, price_details) = api_module.get_flight_details(request.form)
		return render_template('main.html', flight_details=flight_details, price_details = price_details)
