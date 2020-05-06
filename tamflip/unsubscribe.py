from flask import g, render_template, request, url_for, Blueprint
from itsdangerous import URLSafeSerializer, BadData
from tamflip.db import get_db

bp = Blueprint('unsubscribe', __name__, url_prefix="/unsubscribe")


@bp.route('/<token>', methods=['GET', 'POST'])
def index(token):

    # Token verification
    with open('credentials.txt') as f:
        credentials = {k: v for k, v in map(str.split, f.readlines())}
        server_secret = credentials['SERVER_SECRET']

    serializer = URLSafeSerializer(server_secret, salt='unsubscribe')
    try:
        email = serializer.loads(token)
    except BadData as e:
        return 'Invalid token provided'

    # Display unsubscribe page
    if request.method == 'GET':
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
        return render_template(
            'unsubscribe.html',
            flight_details=flight_details
        )

    # Take user input, unsubscribe and display confirmation
    if request.methods == 'POST':
        db = get_db()

        row_ids = request.form.get('ids', [])
        for row_id in row_ids:
            cursor = db.execute(
                """
                SELECT *
                FROM tracked_flights
                WHERE id = ?
                """,
                (row_id)
            )

        print('Deleting the following rows...')
        for row in cursor.fetchall():
            print(tuple(row))

        return 'Success'
