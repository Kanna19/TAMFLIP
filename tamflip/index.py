from flask import g, render_template, request, url_for, Blueprint
from . import api_module
from flask import session
from . import store_info
from .helper_functions import get_airport_codes

bp = Blueprint('index', __name__, url_prefix="/")

@bp.route('/', methods=['GET', 'POST'])
def index():

	airport_codes = get_airport_codes()
	
	if request.method == 'GET':
		return render_template('main.html', airport_codes=airport_codes)

	if request.method == 'POST'
		if(request.form["submit"] =="search"):
			# clear out any files created with session variables if any.
			flight_details, price_details = api_module.get_flight_details(request.form)
			# creates the files to store data for each of the above data
			store_info.create_files(flight_details, price_details)
			return render_template(
				'main.html',
				flight_details=flight_details,
				price_details=price_details,
				airport_codes=airport_codes,
			)
		else:
			# gets back the data accordingly for the session
			flight_details, price_details = store_info.get_data()
			entry_id, email_id = store_info.get_id(request.form)
			store_info.make_entry(email_id, flight_details[entry_id], price_details[entry_id])
			return render_template(
				'main.html',
				flight_details=flight_details,
				price_details=price_details,
				i=True,
				j=True,
				k=True
			)
