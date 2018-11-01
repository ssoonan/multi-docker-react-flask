#!/bin/sh
flask db upgrade;
sleep 3;
exec gunicorn -w 4 -k gevent server:app -b 0.0.0.0:8000