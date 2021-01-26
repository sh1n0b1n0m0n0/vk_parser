from flask_migrate import Migrate
from webapp.models import db
from webapp.forms import QueryForm
from flask import render_template
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    @app.route('/index', methods=('GET', 'POST'))
    def index():
        title = "Анализ комментарий из групп VK"
        form = QueryForm()
        return render_template('index.html', page_title=title, form=form)

    def query_processing():
        pass

    return app

