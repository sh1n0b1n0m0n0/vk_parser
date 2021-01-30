from flask_migrate import Migrate
from webapp.models import db
from webapp.forms import CommentForm
from flask import Flask, request, redirect,  url_for, render_template
from RF_model import conveyor


app = Flask(__name__)
app.config.from_pyfile('config.py')
models.db.init_app(app)
migrate = Migrate(app, models.db)


@app.route('/', methods=['GET', 'POST'])
def index():
    title = "Анализ комментарий из групп VK"
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        sentiment = conveyor(comment)
        if sentiment == 1:
            result = ' - Positive'
            return render_template('solution.html', comment=form.comment.data + result, form=form)
        elif sentiment == 0:
            result = ' - Negative!'
            return render_template('solution.html', comment=form.comment.data + result, form=form)

    return render_template('index.html', page_title=title, form=form)
