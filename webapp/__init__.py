from flask_migrate import Migrate
from flask import Flask, render_template
from webapp.models import db
from webapp.forms import QueryForm

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    @app.route('/index')
    def index():
        title = "Анализ комментарий из групп VK."
        query = QueryForm()
        return render_template('index.html', page_title=title, form=query)

    return app

