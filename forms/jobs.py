from flask_wtf import FlaskForm
import wtforms
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = StringField("Job title", validators=[DataRequired()])
    job = StringField("Team leader id", validators=[DataRequired()])
    work_size = StringField("Work size", validators=[DataRequired()])
    collaborators = StringField("Collaborators", validators=[DataRequired()])
    is_finished = wtforms.SelectField("Is job finished?")
    submit = SubmitField("Submit")