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

- Third, collect static files for admin panel
```text
./manage.py collectstatic
```

- Fourth, run tests
```text
./manage.py test apps.bikes.tests
```