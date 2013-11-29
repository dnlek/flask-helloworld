import unittest
import json
from flask import Flask
from flask_testing import TestCase
from app import create_app

class FlaskrTestCase(TestCase):

    def create_app(self):
        return create_app()

    def test_hello(self):
        rv = self.client.get('/')
        assert rv.status == '200 OK'
        assert 'Hello World!' in rv.data

    def test_tasks(self):
        t = self.client.application.db.Task()
        t.title = u"test"
        t.save()
        tasks = self.client.application.db.Task.find()

        rv = self.client.get('/tasks')
        d = json.loads(rv.data)
        assert len(d) == tasks.count()


if __name__ == '__main__':
    unittest.main()
