from webapp.models import db
from flask import Flask
from

app = Flask(__name__)
db.create_all(app=create_app())