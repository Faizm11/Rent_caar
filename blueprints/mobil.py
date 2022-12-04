from flask import Blueprint, render_template, request, redirect, flash, url_for
from models.user_admin import User 
from models.mobil import Cars
from werkzeug.utils import secure_filename
import os
from extensions import UPLOAD_FOLDER, db
from form.formmobil import Carsform
mobil_blueprint = Blueprint("mobil_blueprint",__name__)

@mobil_blueprint.route('/mobil')
def home():
    print("bisa")
    return render_template("index.html")

@mobil_blueprint.route ('/carform')
def carform():
    form = Carsform()   
    return render_template('carform.html',form=form)

@mobil_blueprint.route ('/carform/create', methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form['name_mobil']
        colour =request.form['colour_mobil']
        price = request.form['price_mobil']
        category_id = request.form['category_id']
        Obj = Cars(name=name, colour=colour, price=price, category_id=category_id)
        db.session.add(Obj)
        db.session.commit()
        return redirect('/carform')
