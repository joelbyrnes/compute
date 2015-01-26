# Distributed JavaScript computing

Experiments in parallel computing using JavaScript and browsers

Parallel.js included from https://github.com/adambom/parallel.js

## Quick start

These instructions are for Linux but windows equivalents probably work.

* clone repo
* pull in dependencies: git submodule update --init
* python manage.py makemigrations
* python manage.py migrate
* python manage.py loaddata compute/fixtures/examples.json
* python manage.py runserver
* Browse to http://localhost:8000/compute

Make the server available beyond localhost with: python manage.py runserver 0.0.0.0:8000
