import pickle
import os
from flask import session
from tamflip.db import get_db

def hashObject(object):
	return str(hash(object))+'.txt.dummyfile'

def get_id(my_dict):
	for key in my_dict:
		if my_dict[key] != '':
			return (int(key[5:]), my_dict[key])

def create_files(flight_details, price_details):
	filelist = [ f for f in os.listdir('./') if f.endswith(".dummyfile") ]
	for f in filelist:
	    os.remove(os.path.join('./', f))
	# create the new hashes for the objects
	flight_file = hashObject(str(flight_details))
	price_file = hashObject(str(price_details))
	# store the hash in the session variables
	session["flight_file"] = flight_file
	session["price_file"] = price_file
	# store the data into the files
	with open(flight_file, 'wb') as config_dictionary_file:
		pickle.dump(flight_details, config_dictionary_file)
	with open(price_file, 'wb') as config_dictionary_file:
		pickle.dump(price_details, config_dictionary_file)

def get_data():
	flight_details, price_details = ([], [])
	if(os.path.exists(session["flight_file"]) and
		os.path.exists(session["price_file"])):
		with open(session["flight_file"], 'rb') as f:
			flight_details = pickle.load(f)
		with open(session["price_file"], 'rb') as f:
			price_details = pickle.load(f)
	return flight_details, price_details

def make_entry(email_id, flight_details, price_details):
	db = get_db()
	if len(flight_details) == 2:
		db.execute(
			"""
			INSERT INTO tracked_flights(id,
                                        email,
                                        dept_aircraft_code,
                                        dept_carrier_code,
                                        return_aircraft_code,
                                        return_carrier_code,
                                        adults,
                                        children,
                                        infants,
                                        from_location,
                                        to_location,
                                        departure_date,
                                        return_date,
                                        type_of_class,
                                        prev_price)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
			""",
			(None,
			 email_id,
			 flight_details[0]['aircraft_code'],
			 flight_details[0]['carrier_code'],
			 flight_details[1]['aircraft_code'],
			 flight_details[1]['carrier_code'],
			 flight_details[0]['adults'],
			 flight_details[0]['children'],
			 flight_details[0]['infants'],
			 flight_details[0]['from_location'],
			 flight_details[0]['to_location'],
			 flight_details[0]['departure_date'],
			 flight_details[0]['return_date'],
			 flight_details[0]['type_of_class'],
			 str(price_details))
		)
	else:
		db.execute(
			"""
			INSERT INTO tracked_flights(id,
                                        email,
                                        dept_aircraft_code,
                                        dept_carrier_code,
                                        return_aircraft_code,
                                        return_carrier_code,
                                        adults,
                                        children,
                                        infants,
                                        from_location,
                                        to_location,
                                        departure_date,
                                        return_date,
                                        type_of_class,
                                        prev_price)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
			""",
			(None,
			 email_id,
			 flight_details[0]['aircraft_code'],
			 flight_details[0]['carrier_code'],
			 None,
			 None,
			 flight_details[0]['adults'],
			 flight_details[0]['children'],
			 flight_details[0]['infants'],
			 flight_details[0]['from_location'],
			 flight_details[0]['to_location'],
			 flight_details[0]['departure_date'],
			 None,
			 flight_details[0]['type_of_class'],
			 str(price_details))
		)

	print('Entry made into DB')
	db.commit()

# returns if an entry exists in the DB already or not
def entry_exists(email_id, flight_details):
	db = get_db()
	if len(flight_details) == 2:
		round_entry = (
			email_id,
			flight_details[0]['aircraft_code'],
			flight_details[0]['carrier_code'],
			flight_details[1]['aircraft_code'],
			flight_details[1]['carrier_code'],
			flight_details[0]['adults'],
			flight_details[0]['children'],
			flight_details[0]['infants'],
			flight_details[0]['from_location'],
			flight_details[0]['to_location'],
			flight_details[0]['departure_date'],
			flight_details[0]['return_date'],
			flight_details[0]['type_of_class'],
		)

		row = db.execute(
			"""
			SELECT *
			FROM tracked_flights
			WHERE
				email = ?
			AND
				dept_aircraft_code = ?
			AND
				dept_carrier_code = ?
			AND
				return_aircraft_code = ?
			AND
				return_carrier_code = ?
			AND
				adults = ?
			AND
				children = ?
			AND
				infants = ?
			AND
				from_location = ?
			AND
				to_location = ?
			AND
				departure_date = ?
			AND
				return_date = ?
			AND
				type_of_class = ?
			""",
		round_entry
		).fetchall()

		return (len(row) != 0)

	else:
		one_way_entry = (
			email_id,
			flight_details[0]['aircraft_code'],
			flight_details[0]['carrier_code'],
			flight_details[0]['adults'],
			flight_details[0]['children'],
			flight_details[0]['infants'],
			flight_details[0]['from_location'],
			flight_details[0]['to_location'],
			flight_details[0]['departure_date'],
			flight_details[0]['type_of_class'],
		)

		row = db.execute(
			"""
			SELECT *
			FROM tracked_flights
			WHERE
				email = ?
			AND
				dept_aircraft_code = ?
			AND
				dept_carrier_code = ?
			AND
				adults = ?
			AND
				children = ?
			AND
				infants = ?
			AND
				from_location = ?
			AND
				to_location = ?
			AND
				departure_date = ?
			AND
				type_of_class = ?
			""",
		one_way_entry
		).fetchall()

		return (len(row) != 0)
