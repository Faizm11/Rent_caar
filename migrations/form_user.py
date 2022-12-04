from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DateField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, Length

class UsersFormLogin(FlaskForm):
    name = StringField("Nama",validators=[InputRequired(), Length(min=1)])
    p = PasswordField( "Password", validators=[InputRequired(), Length(min=1)])
    email = StringField( "Email", validators=[InputRequired(), Length(min=1)])
