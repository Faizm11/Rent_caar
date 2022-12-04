from extensions import db 
from flask_login import (LoginManager, UserMixin, login_required, login_user, logout_user)

class User(UserMixin,db.Model):
    __tablename__ ="users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(233), nullable=False)
    email = db.Column(db.String(255), nullable=True)