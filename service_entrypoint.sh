#!/bin/bash

sleep 10
npm install
npm run build
alembic upgrade head

cd /app/web2py
python web2py.py -a 'admin' -i 0.0.0.0 -p 8000
tail -f /dev/null
