import imp
from flask import Flask
from extensions import *
from blueprints.admin import admin_blueprint
from models import *  
from blueprints.mobil import mobil_blueprint
from blueprints.login_admin import regis_blueprint
from blueprints.admincat import category_blueprint
app = Flask(__name__)

app.config['SECRET_KEY'] = 'rahasia'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:faiz@localhost/faiz15"



db.init_app(app)
migrate.init_app(app=app, db=db)
login_manager.init_app(app=app)


app.register_blueprint(admin_blueprint)
app.register_blueprint(mobil_blueprint)
app.register_blueprint(regis_blueprint)
app.register_blueprint(category_blueprint)


if __name__ == '__main__':
    app.run(debug=True)