#A python3-flask pastebin

Example: https://cpy.pt/

##Dependencies

* postgresql-9.5 <
* python3 (3.3+)
* python3-flask
* python3-pygments
* python3-psycopg2

##Installation

* install dependencies
	* ```
		pip install -r requirements.txt
		```
* setup db with schema.sql
	* ```
		sudo -u postgres psql -f schema.db
		```
* copy config.py.example as config.py
	* ```
		cp config.py.example config.py
		```
* configure config.py - **make sure secret_key and domain are changed!**
* use whatever wsgi server you want - (gunicorn!)
