from flask import g, render_template, request, url_for, Blueprint
from . import api_module
from tamflip.db import get_db
from hashlib import md5

bp = Blueprint('subscribe', __name__, url_prefix="/subscribe")

def generate_code(str):
	#Add salt
	str = str + "jai_nithin_anudeep_rebu"
	return md5(str.encode()).hexdigest()


@bp.route('/')
def index():
	print("In subscribe")
	#Sessions variables might be better
	if request.method == 'GET':
		print("In GET method I am")
		email = request.args.get('email', None)

		print("Email: ", email)
		print(generate_code(email))

		print("Type: ", type(generate_code(email)))

		if email == None:
			#Handle empty value
			return ""

		#Add to user_details database
		db = get_db()
		#Check if already in database
		if db.execute("SELECT email FROM user_details WHERE email = ?", (email,)).fetchone() is None:
			db.execute("INSERT INTO user_details VALUES (?, ?)", (email, generate_code(email)))

		#Checking insertion
		val = db.execute("SELECT * FROM user_details").fetchall()
		for i in val:
			print(tuple(i))



		#Add data to tracked flights
		return "Done"
