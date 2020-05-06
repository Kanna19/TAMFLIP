from flask import g, render_template, request, url_for, Blueprint
from . import api_module
from .helper_functions import get_airport_codes

bp = Blueprint('index', __name__, url_prefix="/")


@bp.route('/', methods=['GET', 'POST'])
def index():

	airport_codes = get_airport_codes()
	
	if request.method == 'GET':
		return render_template('main.html', airport_codes=airport_codes)

	if request.method == 'POST':
		if request.form["submit"] == "search":
			flight_details, price_details = api_module.get_flight_details(request.form)
			return render_template(
				'main.html',
				flight_details=flight_details,
				price_details=price_details,
				airport_codes=airport_codes,
			)
		else:
			# see if all the ids' are empty.
			# see the id which is not empty.
			return request.form
