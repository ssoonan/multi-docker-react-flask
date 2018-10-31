#!/bin/sh
flask db migrate;
flask db upgrade;
sleep 3;
exec gunicorn -w 4 -k gevent server.py:app