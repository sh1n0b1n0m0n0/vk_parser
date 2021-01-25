from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class QueryForm(FlaskForm):
    user_query = StringField('Давай оценим твоё предложение', render_kw={'class': 'form-control'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})
