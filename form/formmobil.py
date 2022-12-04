from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DateField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, Length


class CategoryForm(FlaskForm):
    name = StringField("name_c", validators=[InputRequired(), Length(min=1)])  

class Carsform(FlaskForm):	
    name_mobil = StringField("Nama", validators=[InputRequired(), Length(min=1)])    
    colour_mobil = StringField("Warna", validators=[InputRequired(), Length(min=1)])  
    price_mobil  = IntegerField("Harga", validators=[InputRequired()])
    category_id = StringField("Category", validators=[InputRequired()])

