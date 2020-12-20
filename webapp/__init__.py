from flask_migrate import Migrate
from flask import Flask, render_template
from webapp.models import db


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
