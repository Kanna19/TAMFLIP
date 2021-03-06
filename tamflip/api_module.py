import requests
import json
import isodate
from flask import session

# Getting an access token given API_KEY and API_SECRET
def get_token():
	url_post = 'https://test.api.amadeus.com/v1/security/oauth2/token'
	param_object_post = {
		'grant_type': 'client_credentials',
		'client_id':'0PsAsVqdGcnL8Mm8CnbWWgL58Q1OrYuA',
		'client_secret':'zzrL2xqaJLkebOE2'
	}
	x_post = requests.post(url_post, data=param_object_post)
	y_post = x_post.json()
	access_token = y_post['access_token']
	session['api_token'] = access_token
	return access_token

# Checking if an access token is valid or not
def check_valid_token(access_token):
	url_get_valid = 'https://test.api.amadeus.com/v1/security/oauth2/token/'
	url_get_valid += access_token
	x_get_valid = requests.get(url_get_valid)
	y_get_valid = x_get_valid.json()
	return (y_get_valid['state'] == 'approved')

def class_of_travel(travel_class):
	return {
		'Economy': 'ECONOMY',
		'Premium Economy': 'PREMIUM_ECONOMY',
		'Business': 'BUSINESS',
		'First Class': 'FIRST'
	}[travel_class]

# makes a call and returns the flightDetails filled in the form
def get_flight_details(form_object):
	if("api_token" in session and check_valid_token(session["api_token"])):
		access_token = session["api_token"]
	else:
		access_token = get_token()
	# prepare URL for sending
	url_get_flight = (
		'https://test.api.amadeus.com/v2/shopping/flight-offers?'
		+ '&originLocationCode=' + form_object['from_location']
		+ '&destinationLocationCode=' + form_object['to_location']
		+ '&departureDate=' + form_object['departure_date']
		+ ('' if (form_object['return_date'] is None
					or form_object['return_date'] == '')
		   else '&returnDate=' + form_object['return_date'])
		+ '&travelClass=' + class_of_travel(form_object['type_of_class'])
		+ '&adults=' + str(form_object['adults'])
		+ '&children=' + str(form_object['children'])
		+ '&infants=' + str(form_object['infants'])
		+ '&currencyCode=' + 'INR'
	)

	response = requests.get(
		url_get_flight,
		headers={'Authorization': 'Bearer ' + str(access_token)}
	)

	if response.status_code != 200:
		return ([], [])

	flight_offers = response.json()

	# In case of no flights detected
	if flight_offers['meta']['count'] == 0:
		return ([], [])

	# We get a success response
	flight_details, price_details = preprocess_json(form_object, flight_offers)
	# print(flight_details)
	return (flight_details, price_details)

# preprocess the JSON object into a clean list
def preprocess_json(form_object, flight_offers):
	# map carrier codes to carrier names
	carrier_map = flight_offers['dictionaries']['carriers']

	flight_details = []
	price_details = []
	# store all the flight details into a dictionary
	for flight_offer in flight_offers['data']:
		temp_list = []
		# stores one round trip if there
		for itinerary in flight_offer['itineraries']:
			temp_dict = {
				'departure_time': isodate.parse_datetime(itinerary['segments'][0]['departure']['at']),
				'arrival_time': isodate.parse_datetime(itinerary['segments'][-1]['arrival']['at']),
				'duration': isodate.parse_duration(itinerary['duration']),
				'carrier_code': itinerary['segments'][0]['carrierCode'],
				'carrier_name': carrier_map[itinerary['segments'][0]['carrierCode']],
				'aircraft_code': itinerary['segments'][0]['aircraft']['code'],
				'number_of_stops': str(sum([int(segment['numberOfStops']) for segment in itinerary['segments']])),
				'adults': str(form_object['adults']),
				'children': str(form_object['children']),
				'infants': str(form_object['infants']),
				'from_location': form_object['from_location'],
				'to_location': form_object['to_location'],
				'type_of_class': form_object['type_of_class'],
				'departure_date': form_object['departure_date'],
				'return_date': form_object['return_date']
			}
			temp_list.append(temp_dict)

		price_details.append(flight_offer['price']['total'])
		flight_details.append(temp_list)

	return flight_details, price_details

def query_tracked_flight(user_object):
	flight_details, price_details = get_flight_details(user_object)
	for i, flight in enumerate(flight_details):
		if (flight[0]['carrier_code'] == user_object['dept_carrier_code']
				and flight[0]['aircraft_code'] == user_object['dept_aircraft_code']):
			# If round trip then, check return flight details too
			if len(flight) == 2:
				if(flight[1]['carrier_code'] == user_object['return_carrier_code']
						and flight[1]['aircraft_code'] == user_object['return_aircraft_code']):
					return flight, price_details[i]
			else :
				return flight, price_details[i]

	return [], -1
