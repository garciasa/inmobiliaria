#!/bin/bash
cd /home/ubuntu/inmoviliaria/inmobiliaria
source /home/ubuntu/inmoviliaria/bin/activate
exec gunicorn_django -w 3 --bind=0.0.0.0:8000 --user=ubuntu --group=ubuntu --log-level=debug --log-file=/home/ubuntu/inmoviliaria/logs/gunicorn1.log 2>> /home/ubuntu/inmoviliaria/logs/gunicorn2.log
