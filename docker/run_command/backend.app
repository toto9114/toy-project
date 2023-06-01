#!/bin/bash
set -e
cd ${PROJECT_DIR}
exec su -c "gunicorn -c gunicorn.conf.py foodmapapi.wsgi" jihun
