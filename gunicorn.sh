#!/bin/sh
gunicorn -c gunicorn.conf.py pynomer.app:app
