flask with docker

docker run -it --rm --name flask --mount type=bind,src="$(pwd)",dst=/code -p 5000:5000 python:3.11 bash -c "cd /code && bash

pip install shell
pipenv shell
pipenv install flask

pipenv install python-dotenv
pipenv install flask-cors
pipenv install flask-sqlalchemy 
pipenv install psycopg2-binary

flask run <- runs dev server




https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

pipenv run pip freeze > requirements.txt

use WSGI server for production
gunicorn

for windows use: waitress