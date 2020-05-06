import pickle
import os
from flask import session
from tamflip.db import get_db

def hashObject(object):
	return str(hash(object))+'.txt'

def get_id(my_dict):
	for key in my_dict:
		if(my_dict[key]!=""):
			return (int(key[5:]), my_dict[key])

def create_files(flight_details, price_details):
	# delete the previously hashed files if any
	# if("flight_file" in session):
	# 	os.remove(session["flight_file"])
	# 	os.remove(session["price_file"])
	# 	print("Removed")
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
	# get the data back into the files
	with open(session["flight_file"], 'rb') as f:
		flight_details = pickle.load(f)
	with open(session["price_file"], 'rb') as f:
		price_details = pickle.load(f)
	return flight_details, price_details

def make_entry(email_id, flight_details, price_details):	
	db = get_db()
	print(flight_details)
	print(price_details)
	if(len(flight_details)==2):
		db.execute(
		'insert into tracked_flights(id,email,dept_aircraft_code,dept_carrier_code,return_aircraft_code,return_carrier_code, adults, children, infants,from_location,to_location,departure_date,return_date, type_of_class, prev_price) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
		(
			(None,email_id, flight_details[0]['aircraft_code'],flight_details[0]['carrier_code'], 
				flight_details[1]['aircraft_code'], flight_details[1]['carrier_code'], 
				flight_details[0]['adults'], flight_details[0]['children'], flight_details[0]['infants'], 
				flight_details[0]['from_location'], flight_details[0]['to_location'], flight_details[0]['departure_date'], 
				flight_details[0]['return_date'], flight_details[0]['type_of_class'], str(price_details))
		)
		)
		print("Made round-trip entry")
	else:
		db.execute(
		'insert into tracked_flights(id,email,dept_aircraft_code,dept_carrier_code,return_aircraft_code,return_carrier_code, adults, children, infants,from_location,to_location,departure_date,return_date, type_of_class, prev_price) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
		(
			(None,email_id, flight_details[0]['aircraft_code'],flight_details[0]['carrier_code'], 
				None, None, flight_details[0]['adults'], flight_details[0]['children'], flight_details[0]['infants'], 
				flight_details[0]['from_location'], flight_details[0]['to_location'], flight_details[0]['departure_date'], 
				None, flight_details[0]['type_of_class'], str(price_details))
		)
		)
		print("Made one-way entry")
