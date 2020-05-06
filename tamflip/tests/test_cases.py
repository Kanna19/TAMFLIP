import os
import unittest
import tempfile

from tamflip import create_app
from tamflip.db import get_db
from tamflip.db import init_db

with open(os.path.join(os.path.dirname(__file__), "test_data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")

class TestCases(unittest.TestCase):

    def setUp(self):
        """Method called prior each unittest execution"""
        self.db_fd, self.db_path = tempfile.mkstemp()
        app = create_app({'TESTING': True, 'DATABASE': self.db_path})
        with app.app_context():
            # NOTE:
            # Make sure that insert commands in schema.sql are commented or removed
            init_db()
            get_db().executescript(_data_sql)

        self.app = app.test_client()

    def tearDown(self):
        """Method called after each unittest execution"""
        os.close(self.db_fd)
        os.unlink(self.db_path)

    # Add test cases using prefix test_
    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Tamflip!', response.data)
        self.assertIn(b'From', response.data)
        self.assertIn(b'Destination', response.data)

    def test_invalid_unsubscribe_token(self):
        response = self.app.get('/unsubscribe/1')
        self.assertIn(b'Invalid token', response.data)

if __name__ == '__main__':
    unittest.main()
