from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text, MetaData, Table, DateTime, Boolean
from webapp import config

db = SQLAlchemy()

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
