import os
import unittest
import tempfile

from tamflip import create_app
from tamflip.db import get_db
from tamflip.db import init_db
from tamflip.helper_functions import captured_output
from tamflip.flight_tracker import send_alerts_to_subscribed_users
from tamflip.expired_entries_cleanup import remove_outdated_entries

with open(os.path.join(os.path.dirname(__file__), 'test_data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

with open(os.path.join(os.path.dirname(__file__), 'test_data_email.sql'), 'rb') as f:
    _data_sql_email = f.read().decode('utf8')

with open(os.path.join(os.path.dirname(__file__), 'test_data_expired_entry.sql'), 'rb') as f:
    _data_sql_expired_entry = f.read().decode('utf8')

class TestCases(unittest.TestCase):

    def setUp(self):
        """Method called prior each unittest execution"""
        self.db_fd, self.db_path = tempfile.mkstemp()
        app = create_app({'TESTING': True, 'DATABASE': self.db_path})
        with app.app_context():
            # NOTE: Make sure that insert commands in schema.sql are commented or removed
            init_db()
            get_db().executescript(_data_sql)

        self.app = app
        self.app_client = app.test_client()
        self.tokens = {
            'test_unsubscribe':
                'InRlc3Rib2lAdGVzdGJvaS5jb20i.cshVCqvl20ukOAh1Tgv53NDtjQk',
            'test_flightstatus':
                'InRlc3Rib2lAdGVzdGJvaS5jb20i.jTrlhxNTqHIsz3kTVweRT9pUo18',
            'evil_unsubscribe':
                'ImV2aWxib2lAZXZpbGJvaS5jb20i.lMCPwRVp2XAOSqaJzGccdyDQtcE'
        }

    def tearDown(self):
        """Method called after each unittest execution"""
        os.close(self.db_fd)
        os.unlink(self.db_path)

    # Add test cases using prefix test_
    def test_main_page(self):
        """Test if main page is loading when GET request is sent"""
        response = self.app_client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Tamflip!', response.data)
        self.assertIn(b'From', response.data)
        self.assertIn(b'Destination', response.data)

    def test_main_page_search_flights(self):
        """Test if main page returns search results"""
        response = self.app_client.post(
            '/',
            data={
                'from_location': 'Hyderabad (HYD)',
                'to_location': 'Bangalore (BLR)',
                'departure_date': '2020-05-20',
                'return_date': '',
                'type_of_class': 'Economy',
                'adults': 1,
                'children': 0,
                'infants': 0,
                'submit': 'search',
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'May 20', response.data)

    def test_no_flights_returned(self):
        """Test the case in which no flights are returned for the given search query"""
        response = self.app_client.post(
            '/',
            data={
                'from_location': 'Aasiaat, Greenland (JEG)',
                'to_location': 'Pyongyang, North Korea (FNJ)',
                'departure_date': '2020-05-22',
                'return_date': '',
                'type_of_class': 'Economy',
                'adults': 1,
                'children': 0,
                'infants': 0,
                'submit': 'search',
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No results to show', response.data)

    def test_track_flights(self):
        """Test the case in which we track a flight not already tracking"""

        # Search
        response = self.app_client.post(
            '/',
            data={
                'from_location': 'Hyderabad (HYD)',
                'to_location': 'Bangalore (BLR)',
                'departure_date': '2020-05-20',
                'return_date': '2020-05-21',
                'type_of_class': 'Economy',
                'adults': 1,
                'children': 0,
                'infants': 0,
                'submit': 'search',
            }
        )
        self.assertEqual(response.status_code, 200)

        # Track
        response = self.app_client.post(
            '/',
            data={
                'email1': 'dummy_mail@mail.com'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"entry_there": false', response.data)
        self.assertIn(b'"tracked_flight": "1"', response.data)

    def test_already_track_flights(self):
        """Test the case in which we track a flight already tracking"""

        # Search
        response = self.app_client.post(
            '/',
            data={
                'from_location': 'Hyderabad (HYD)',
                'to_location': 'Bangalore (BLR)',
                'departure_date': '2020-05-20',
                'return_date': '',
                'type_of_class': 'Economy',
                'adults': 1,
                'children': 0,
                'infants': 0,
                'submit': 'search',
            }
        )
        self.assertEqual(response.status_code, 200)

        # Track
        response = self.app_client.post(
            '/',
            data={
                'email1': 'dummy_mail@mail.com'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"entry_there": false', response.data)
        self.assertIn(b'"tracked_flight": "1"', response.data)

        # Track Again
        response = self.app_client.post(
            '/',
            data={
                'email1': 'dummy_mail@mail.com'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"entry_there": true', response.data)
        self.assertIn(b'"tracked_flight": "1"', response.data)

    def test_unsub_page_valid_token(self):
        """Test if unsubscribe page loads when valid token is provided"""
        response = self.app_client.get(
            '/unsubscribe/' + self.tokens['test_unsubscribe']
        )
        self.assertEqual(response.status_code, 200)

    def test_unsub_page_invalid_token(self):
        """Test if unsubscribe page loads when invalid token is provided"""
        response = self.app_client.get('/unsubscribe/1')
        self.assertIn(b'Invalid token', response.data)

    def test_unsub_page_valid_flights(self):
        """Test if unsubscribe page contains all the subscribed flights"""
        response = self.app_client.get(
            '/unsubscribe/' + self.tokens['test_unsubscribe']
        )
        self.assertIn(b'Flight1', response.data)
        self.assertIn(b'Flight2', response.data)

    def test_unsub_update(self):
        """Test if the unsubbed data has been updated when page is visited again"""
        response = self.app_client.post(
            '/unsubscribe/' + self.tokens['test_unsubscribe'],
            data={'8': 'off', '9': 'on'}
        )
        # Check if info has been updated
        self.assertNotIn(b'Flight1', response.data)
        self.assertIn(b'Flight2', response.data)

    def test_unsub_others_data(self):
        """Test if a user can unsub other users data"""
        response = self.app_client.post(
            '/unsubscribe/' + self.tokens['evil_unsubscribe'],
            data={'10': 'on', '9': 'off'}
        )
        response = self.app_client.get(
            '/unsubscribe/' + self.tokens['test_unsubscribe']
        )
        self.assertIn(b'Flight2', response.data)

    def test_flightstatus_page_valid_token(self):
        """Test if flight status page loads when valid token is provided"""
        response = self.app_client.get(
            '/flightstatus/' + self.tokens['test_flightstatus']
        )
        self.assertEqual(response.status_code, 200)

    def test_flightstatus_page_invalid_token(self):
        """Test if flight status page loads when invalid token is provided"""
        response = self.app_client.get('/flightstatus/1')
        self.assertIn(b'Invalid token', response.data)

    def test_flightstatus_page_valid_flights(self):
        """Test if flight status page shows the tracked flights"""
        response = self.app_client.get(
            '/flightstatus/' + self.tokens['test_flightstatus']
        )
        self.assertIn(b'2020-05-14', response.data)
        self.assertIn(b'2020-05-16', response.data)

    def test_alerts(self):
        """Test if alert sender function sends email to subscribed users"""
        with captured_output() as (out, err):
            with self.app.app_context():
                init_db()
                get_db().executescript(_data_sql_email)

            send_alerts_to_subscribed_users(self.app)

        output = out.getvalue().strip()
        self.assertIn('Sent email to kannasasuke19@gmail.com', output)

    def test_expired_entries_cleanup(self):
        """Test if the expired entries are removed from database"""
        with captured_output() as (out, err):
            with self.app.app_context():
                init_db()
                get_db().executescript(_data_sql_expired_entry)

            remove_outdated_entries(self.app)

        output = out.getvalue().strip()
        self.assertIn('testboi@testboi.com', output)
        self.assertIn('AUH', output)
        self.assertIn('DOH', output)
        self.assertIn('2020-05-01', output)

if __name__ == '__main__':
    unittest.main()
