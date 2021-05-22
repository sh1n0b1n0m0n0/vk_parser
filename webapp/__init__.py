from flask_migrate import Migrate
from webapp.models import db
from webapp import models
from webapp.forms import CommentForm
from flask import Flask, request, redirect,  url_for, render_template
from RF_model import conveyor


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        title = "Анализ комментарий v1.0."
        form = CommentForm()
        if form.validate_on_submit():
            comment = form.comment.data
            sentiment = conveyor(comment)
            if sentiment == 1:
                result = ' - Красава! Хороший коммент.'
                return render_template('solution.html', comment=form.comment.data + result, form=form)
            elif sentiment == 0:
                result = ' - Осуждаю! Извинись!'
                return render_template('solution.html', comment=form.comment.data + result, form=form)

        return render_template('index.html', page_title=title, form=form)

    return app