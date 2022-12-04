from flask import Blueprint, render_template, request, redirect, flash, url_for
from models.user_admin import User 
from models.mobil import Category,Cars
from werkzeug.utils import secure_filename
import os 
from form.formmobil import Carsform
from extensions import UPLOAD_FOLDER, db

mobil_bp = Blueprint("mobil_bp",__name__)

@mobil_bp.route('/admin/category/<int:id>/car')
def car(id):
    mobil = Cars.query.filter.by(id=id).first()
    return render_template("cars.html", mobil=mobil)

@mobil_bp.route('/admin/category/<int:id>/car/<int:c_id>/delete')
def delete_cars(id, c_id):
    mobil = Cars.query.filter_by(id=c_id).first()
    db.session.delete(mobil)
    db.session.commit()

@mobil_bp.route('/admin/category/<int:id>/car/create', methods=['POST'])
def create_mobil(id)
