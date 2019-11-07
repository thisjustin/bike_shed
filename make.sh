#!/bin/bash
set -e

sqlite="db.sqlite3"
migrations='apps/bikes/migrations'
[ -f $sqlite ] && rm $sqlite
[ -d "$migrations" ] && rm -Rf $migrations

python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

init() {
  python manage.py collectstatic
  python manage.py makemigrations bikes
  python manage.py migrate bikes
  python manage.py makemigrations
  python manage.py migrate
}

init_unittest() {
  python manage.py test apps.bikes.tests
}

create_objects() {
  python manage.py create_brands_and_bikes
}

init
init_unittest
create_objects
py3clean .

python manage.py runserver
