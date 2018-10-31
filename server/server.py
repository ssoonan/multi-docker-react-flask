from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import redis

app = Flask(__name__)
db = SQLAlchemy(app)
r = redis.StrictRedis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'))


class Values(db.Model):
    values = db.Column(db.Integer)

@app.route('/')
def index():
    return 'Hi'

@app.route('/values/all')
def values_all():
    values = Values.query.all()
    print(jsonify(values))


@app.route('/')
    
    