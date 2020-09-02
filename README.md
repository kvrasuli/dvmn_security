# Security control panel

This is the Django web app to control visits to the bank vault. It connects to the bank's database server, but connection settings are hidden for now, so you can just use the html markup or check how the data models are implemented.

### How to run (if you have proper settings as env variables)

Python3 should be already installed. Then install dependencies:
```
pip install -r requirements.txt
```
Create the following environment variables:
```
SECRET_KEY='app secret key'
DEBUG='debug mode - True or False'
```
Database server connection settings:
```
DB_HOST='database host'
DB_PORT='database port'
DB_NAME='database name'
DB_USER='database username'
DB_PASSWORD='database password'
```
Run the following console command:
```
python3 manage.py runserver
```
Open in your browser https://127.0.0.1:8000.
