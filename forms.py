from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class CommentForm(FlaskForm):
    comment = TextAreaField('Ну давай разберем по частям, тобою написанное!',
                            widget=TextArea(),
                            validators=[DataRequired()],
                            render_kw={'class': 'form-control'})

    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})