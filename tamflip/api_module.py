import requests
import json

# Getting an access token given API_KEY and API_SECRET
def get_token():
	url_post = 'https://test.api.amadeus.com/v1/security/oauth2/token'
	param_object_post = {'grant_type': 'client_credentials', 'client_id':'jwCdvN4AVxtDLPqT7gDQI7Cdf1dlfdbb','client_secret':'rHnOqnhEsGxQhV3f'}
	x_post = requests.post(url_post, data = param_object_post)
	y_post = x_post.json()
	access_token = y_post['access_token']
	return (access_token)

# Checking if an access token is valid or not
def check_valid_token():
	url_get_valid = 'https://test.api.amadeus.com/v1/security/oauth2/token/'
	url_get_valid += access_token
	x_get_valid = requests.get(url_get_valid)
	y_get_valid = x_get_valid.json()
	if(y_get_valid['state']=='approved'):
		return True 
	return False

# makes a call and returns the flightDetails filled in the form
def get_flight_details(form_object): 
	access_token = get_token()
	# prepare URL for sending
	url_get_flight = 'https://test.api.amadeus.com/v2/shopping/flight-offers?'
	url_get_flight +='&originLocationCode='+form_object['from_location']+'&destinationLocationCode='+form_object['to_location']
	url_get_flight += '&departureDate='+form_object['departure_date']
	# check for One-way or not
	if(form_object['type_of_trip'] != 'One way'):
		url_get_flight +='&returnDate='+form_object['return_date']
	url_get_flight += '&adults='+form_object['adults']+'&children='+form_object['children']+'&infants='+form_object['infants']
	url_get_flight += '&currencyCode='+'INR'+'&nonStop=true'
	# input to post request
	x_get_flight = requests.get(url_get_flight, headers={'Authorization': 'Bearer '+ str(access_token)} )
	y_get_flight = x_get_flight.json()
	# In case request is invalid/no response from server
	if(y_get_flight.get("errors") != None):
		return ([] , [])
	# In case of no flights detected
	if(y_get_flight['meta']['count']==0):
		return ([], [])
	# We get a success response
	(flight_details, price_details) = preprocess_json(y_get_flight)
	return (flight_details, price_details)

# preprocess the JSON object into a clean list
def preprocess_json(my_object):
	flight_details = []
	price_details = []
	# map carrier codes to carrier names
	carrier_map = {}
	for obj in my_object['dictionaries']['carriers']:
		carrier_map[obj] = my_object['dictionaries']['carriers'][obj]
	# store all the flight details into a dictionary 
	for obj in my_object['data']:
		temp_list = [] 
		# stores one round trip if there 
		for itineraries in obj['itineraries']:
			temp_dict = {}
			temp_dict['duration'] = itineraries['duration']
			temp_dict['departureTime'] = itineraries['segments'][0]['departure']['at']
			temp_dict['arrivalTime'] = itineraries['segments'][0]['arrival']['at']
			temp_dict['carrierCode'] = itineraries['segments'][0]['carrierCode']
			temp_dict['carrierName'] = carrier_map[temp_dict['carrierCode']]
			temp_dict['aircraftCode'] = itineraries['segments'][0]['aircraft']['code']
			temp_dict['numberOfStops'] = itineraries['segments'][0]['numberOfStops']
			temp_list.append(temp_dict)
		price_details.append(obj['price']['total'])
		flight_details.append(temp_list)
	return (flight_details,price_details)