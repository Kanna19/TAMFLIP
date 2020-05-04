import requests
import json

# Getting an access token given API_KEY and API_SECRET
def getToken():
	urlPost = 'https://test.api.amadeus.com/v1/security/oauth2/token'
	paramObjectPost = {'grant_type': 'client_credentials', 'client_id':'jwCdvN4AVxtDLPqT7gDQI7Cdf1dlfdbb','client_secret':'rHnOqnhEsGxQhV3f'}
	xPost = requests.post(urlPost, data = paramObjectPost)
	yPost = xPost.json()
	accessToken = yPost['access_token']
	return (accessToken)

# Checking if an access token is valid or not
def checkValidToken():
	urlGetValid = 'https://test.api.amadeus.com/v1/security/oauth2/token/'
	urlGetValid += accessToken
	xGetValid = requests.get(urlGetValid)
	yGetValid = xGetValid.json()
	if(yGetValid['state']=='approved'):
		return True 
	return False

# makes a call and returns the flightDetails filled in the form
# needs to be connected with form
def getFlightDetails(formObject): 
	accessToken = getToken()
	urlGetFlight = 'https://test.api.amadeus.com/v2/shopping/flight-offers?'
	urlGetFlight +='&originLocationCode='+formObject['fromLocation']+'&destinationLocationCode='+formObject['destinationLocation']
	urlGetFlight += '&departureDate='+formObject['Travel Date']+'&adults='+formObject['Adults']+'&children='+formObject['Childs']+'&infants='+formObject['Infants']
	urlGetFlight += '&currencyCode='+'INR'+'&nonStop=true'
	xGetFlight = requests.get(urlGetFlight, headers={'Authorization': 'Bearer '+ str(accessToken)} )
	yGetFlight = xGetFlight.json()
	# In case request is invalid/no response from server
	if(yGetFlight.get("errors") != None):
		return []
	# In case of no flights detected
	if(yGetFlight['meta']['count']==0):
		return []
	# We get a success response
	flightDetails = preprocessJson(yGetFlight)
	return flightDetails

# preprocess the JSON object into a clean list
def preprocessJson(myObject):
	flightDetails = []
	# map carrier codes to carrier names
	carrierMap = {}
	for obj in myObject['dictionaries']['carriers']:
		carrierMap[obj] = myObject['dictionaries']['carriers'][obj]
	# store all the flight details into a dictionary 
	for obj in myObject['data']:
		tempDict = {}
		tempDict['duration'] = obj['itineraries'][0]['duration']
		tempDict['departureTime'] = obj['itineraries'][0]['segments'][0]['departure']['at']
		tempDict['arrivalTime'] = obj['itineraries'][0]['segments'][0]['arrival']['at']
		tempDict['carrierCode'] = obj['itineraries'][0]['segments'][0]['carrierCode']
		tempDict['carrierName'] = carrierMap[tempDict['carrierCode']]
		tempDict['aircraftCode'] = obj['itineraries'][0]['segments'][0]['aircraft']['code']
		tempDict['numberOfStops'] = obj['itineraries'][0]['segments'][0]['numberOfStops']
		tempDict['currency'] = obj['price']['currency']
		tempDict['finalPrice'] = obj['price']['total']
		flightDetails.append(tempDict)
	return flightDetails