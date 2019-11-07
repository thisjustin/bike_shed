## Auto deploy:

- Build (will rewrite project database)
```text
./make.sh
```

## Manual deploy:

- First, setup virtual environment 
```text
cd /bike_shed
python3 -m venv venv
source venv/bin/activate
```

- Second, install project requirements
```text
pip install -r requirements.txt
```

- Third, collect static files and make migrations
```text
./manage.py collectstatic
./manage.py manage.py makemigrations
./manage.py manage.py migrate
```

- Fourth, run tests and commands
```text
./manage.py test apps.bikes.tests
./manage.py create_brands_and_bikes
```

- Fifth, run server
```text
./manage.py runserver
```

## Credentials

[Django](http://localhost:8000/admin/)<br/>
You must be logged in to create a bike (superuser credentials)
```text
username: root
password: rootpass
```
