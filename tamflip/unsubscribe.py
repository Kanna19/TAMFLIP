from flask import g, render_template, request, url_for, Blueprint
from itsdangerous import URLSafeSerializer, BadData
from tamflip.db import get_db

bp = Blueprint('unsubscribe', __name__, url_prefix="/unsubscribe")


@bp.route('/<token>', methods=['GET', 'POST'])
def index(token):
    # Display unsubscribe page
    if request.method == 'GET':
        with open('credentials.txt') as f:
            credentials = {k: v for k, v in map(str.split, f.readlines())}
            server_secret = credentials['SERVER_SECRET']

        # Verify token
        serializer = URLSafeSerializer(server_secret, salt='unsubscribe')
        try:
            email = serializer.loads(token)
        except BadData as e:
            print(e)
            return 'Invalid token provided'

        # Get tracked flights
        db = get_db()
        cursor = db.execute(
            """
            SELECT *
            FROM tracked_flights
            WHERE email = ?
            """,
            (email,)
        )
        column_names = list(map(lambda x: x[0], cursor.description))
        flight_details = [
            {k: v for k, v in zip(column_names, tuple(row))}
            for row in cursor.fetchall()
        ]
        print(flight_details)
        return 'Bobby is ready with flight details'
        # return render_template(
        #     'unsubscribe.html',
        #     flight_details=flight_details
        # )

    # Take user input, unsubscribe and display confirmation
    if request.methods == 'POST':
        # TODO
        pass
