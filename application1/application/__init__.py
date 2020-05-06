from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#object gets created from the class of FLask import name


app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

db = SQLAlchemy(app)




from application import routes
# this needs to always be at the end or it will be an infinite loop
