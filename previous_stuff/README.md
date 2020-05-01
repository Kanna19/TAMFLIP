# TAMFLIP
Project for the course CS4443

### API list

**Note**: Please find and add other APIs which we can use. You can search for them [here](https://www.programmableweb.com/category/air-travel/api).

URL | Comments
--- | ---
https://developers.amadeus.com/self-service/category/air | Can do airport autocomplete and nearest airport search. Rate limits per month: 2000 for flight search, 10000 for autocomplete and nearest airport
https://developer.lufthansa.com | Rate limit: 5 calls per second, 1000 calls per hour
https://developer.singaporeair.com/docs/flight_search/ | Rate limit: 1 call per second, 100 calls per day
https://developer.laminardata.aero/documentation/flightdata | 14 day free trail activated
[Sabre travel seasonality](https://developer.sabre.com/docs/rest_apis/air/intelligence/travel_seasonality/reference-documentation#/default/travelSeasonality) | We can get traffic volume rating for each week of the year for a given destination
[Sabre travel instaflights](https://developer.sabre.com/docs/rest_apis/air/search/instaflights_search/reference-documentation#/default/instaFlightsSearch) | This retrieves roundtrip or one-way flight itineraries with published fares and fare breakdowns for a given city pair and departure date.
[Sabre destination finder](https://developer.sabre.com/docs/rest_apis/air/search/destination_finder) | Gives the cheapest destination given an origin airport
