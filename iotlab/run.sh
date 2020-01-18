#!/bin/bash
killall gunicorn
nohup gunicorn --bind 127.0.0.1:8000 wsgi >run.log 2>&1 &
