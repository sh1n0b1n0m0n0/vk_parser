from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class QueryForm(FlaskForm):
    user_query = StringField('Оценим предложение')
    submit = SubmitField('Отправить')
