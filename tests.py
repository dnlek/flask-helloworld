import unittest
from flask_testing import TestCase
from app import create_app


class FlaskTestCase(TestCase):

    def create_app(self):
        return create_app()

    def test_hello(self):
        rv = self.client.get('/')
        assert rv.status == '200 OK'
        assert 'Hello World!' in rv.data

if __name__ == '__main__':
    unittest.main()
