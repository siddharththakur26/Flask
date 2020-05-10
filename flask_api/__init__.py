from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='0a664c9a12fd9c1237822a63aa88b3f6'
'''
import secrets
secrets.token_hex(16)
'''
# Instantiate the database to store image files. (For future Scope)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flask_api import routes