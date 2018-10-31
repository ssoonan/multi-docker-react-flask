from flask import Flask
import redis
import os

r = redis.StrictRedis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'))
p = r.pubsub()

def fib(index):
    if index < 2:
        return 1
    return fib(index - 1) + fib(index - 2)

p.listen