from flask import g, render_template, request, url_for, Blueprint
from itsdangerous import URLSafeSerializer, BadData
from flask import current_app

from tamflip.api_module import query_tracked_flight
from tamflip.flight_tracker import get_tracked_flights

bp = Blueprint('flightstatus', __name__, url_prefix="/flightstatus")


@bp.route('/<token>', methods=['GET'])
def index(token):
    # Token verification
    with open('credentials.txt') as f:
        credentials = {k: v for k, v in map(str.split, f.readlines())}
        server_secret = credentials['SERVER_SECRET']

    serializer = URLSafeSerializer(server_secret, salt='flightstatus')
    try:
        email = serializer.loads(token)
    except BadData as e:
        return 'Invalid token provided'

    flight_statuses = []
    for flight in get_tracked_flights(current_app, email):
        flight_details, curr_price = query_tracked_flight(flight)
        flight_statuses.append(
            (flight_details, float(flight['prev_price']), float(curr_price))
        )

    print(flight_statuses)
    return render_template(
        'flight_email.html',
        flight_statuses=flight_statuses
    )
