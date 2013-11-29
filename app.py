import os
import json
from datetime import datetime
from flask import Flask, Response
from flask.ext.mongokit import MongoKit, Document


class Task(Document):
    __collection__ = 'tasks'
    structure = {
        'title': unicode,
        'creation': datetime,
    }
    required_fields = ['title', 'creation']
    default_values = {'creation': datetime.utcnow()}
    use_dot_notation = True


def create_app():
    app = Flask(__name__)
    app.config.setdefault('MONGODB_HOST', os.environ.get('MONGODB_HOST', '127.0.0.1'))
    app.config.setdefault('MONGODB_PORT', os.environ.get('MONGODB_PORT', 27017))
    app.config.setdefault('MONGODB_DATABASE', os.environ.get('MONGODB_DATABASE', 'flask'))

    db = MongoKit(app)
    db.register([Task])

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    @app.route('/tasks')
    def list_tasks():
        tasks = db.Task.find()
        ret = [{'title': task.title, 'creation': task.creation.strftime('%Y-%m-%d %H:%M')} for task in tasks]
        return Response(response=json.dumps(ret), status=200)

    app.db = db

    return app
