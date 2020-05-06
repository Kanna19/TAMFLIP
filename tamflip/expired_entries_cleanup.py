from tamflip.db import get_db

def remove_outdated_entries(app):
    print('Started cron job which cleans out of date database entries')

    with app.app_context():
        db = get_db()

        # Select Query to check which rows will be deleted
        # This is done because delete statement has no output clause and we
        # need to see what all rows got deleted. https://stackoverflow.com/a/43211369
        cursor = db.execute(
            """
            SELECT *
            FROM tracked_flights
            WHERE
                (return_date IS NULL AND date('now') > departure_date)
            OR
                (return_date IS NOT NULL AND date('now') > return_date)
            """
        )

        print('Deleting the following rows...')
        for row in cursor.fetchall():
            print(tuple(row))

        # Query to delete out of date entries
        db.execute(
            """
            DELETE
            FROM tracked_flights
            WHERE
                (return_date IS NULL AND date('now') > departure_date)
            OR
                (return_date is NOT NULL AND date('now') > return_date)
            """
        )
        db.commit()
        print('Out of date entries deleted.')
