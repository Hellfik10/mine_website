from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    title = StringField('Описание работы', validators=[DataRequired()])
    team_leader = IntegerField("ID командира работы")
    work_size = IntegerField("Время")
    collaborators = StringField("Коллаборации")
    is_finished = BooleanField("Личное")
    submit = SubmitField('Применить')