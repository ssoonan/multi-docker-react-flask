from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.http import HTTP_STATUS_CODES
import os
import redis

app = Flask(__name__)
r = redis.StrictRedis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'))
p = r.pubsub()
app.config.update({
    'SQLALCHEMY_DATABASE_URI': 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
        dbuser=os.environ.get('DB_USER'),
        dbpass=os.environ.get('DB_PASS'),
        dbhost=os.environ.get('DB_HOST'),
        dbname=os.environ.get('DB_NAME')
    ),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
})
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Values(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)

def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
        response = jsonify(payload)
        response.status_code = status_code
    return response


@app.route('/')
def index():
    return 'Hi'

@app.route('/values/all')
def values_all():
    values_all = Values.query.all()
    numbers = [{'numbers': int(value.number) for value in values_all}]
    return jsonify(numbers)


@app.route('/values/current')
def current():
    before_values = r.hgetall('values')
    after_values = {field.decode(): values.decode() for field, values in before_values.items()}
    return jsonify(after_values)


@app.route('/values', methods=['POST'])
def post_values():
    index = int(request.get_json()['index'])
    if index > 40:
        response = error_response(422, 'Index too high')
        return response

    r.hset('values', index, 'Nothing yet!')
    r.publish('insert', index)
    value = Values(number=index)
    db.session.add(value)
    db.session.commit()
    return jsonify({'working': True})



