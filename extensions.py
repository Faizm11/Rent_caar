from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_wtf import CSRFProtect
import os
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = basedir+'/static/media/'