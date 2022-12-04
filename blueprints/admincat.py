from flask import Blueprint, render_template, request, redirect, flash, url_for
from models.user_admin import User 
from models.mobil import Category,Cars
from werkzeug.utils import secure_filename
import os 
from form.formmobil import CategoryForm

from extensions import UPLOAD_FOLDER, db

category_blueprint = Blueprint("category_blueprint",__name__)

@category_blueprint.route('/admin/category')
def categories():
    categories = Category.query.all()
    return render_template ("categories.html", categories=categories) 

@category_blueprint.route('/admin/category/create/', methods=['GET','POST'])
def create_category():
    if request.method == "POST":
        form = CategoryForm()
        categories = Category(name=form.name.data)
        db.session.add(categories)
        db.session.commit()
        return redirect ('/admin/category')
    form = CategoryForm()
    return render_template('cat_form.html', form=form)

@category_blueprint.route('/admin/category/<int:id>/delete')
def delet_category(id):
    categories = Category.query.filter_by(id=id).first()
    db.session.delete(categories)
    db.session.commit()
    return redirect('/admin/category')

@category_blueprint.route('/admin/category/<int:id>/update', methods =['GET','POST'])
def update_category(id):
    categories = Category.query.filter_by(id=id).first()
    if request.method=='POST':
        form = CategoryForm()
        categories.name = form.name.data
        db.session.add(categories)
        db.session.commit()
        return redirect('/admin/category')
    form = CategoryForm(name=categories.name)
    return render_template("cat_update.html", form=form, id=id)
