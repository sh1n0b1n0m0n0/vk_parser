from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text, MetaData, Table, DateTime, Boolean
from webapp import config

db = SQLAlchemy(Flask(__name__))

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def index():
        title = "Комментарии"
        return render_template('index.html', page_title=title)

    return app

class Group(db.Model):
    __tablename__ = 'groups'

    group_id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String, unique=True, nullable=False)
    group_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Группа {} {}>'.format(self.group_name, self.domain)


class Post(db.Model):
    __tablename__ = 'posts'

    group_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.String, nullable=True)
    likes = db.Column(db.Integer, nullable=False)


class Comment(db.Model):
    __tablename__ = 'comments'

    post_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    comment_text = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    sentiment = db.Column(db.Boolean, nullable=True)
