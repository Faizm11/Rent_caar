from flask import Blueprint, render_template, request, redirect, flash, url_for
from models.user_admin import User 
from models.mobil import Category,Cars
from werkzeug.utils import secure_filename
import os
from extensions import UPLOAD_FOLDER, db

admin_blueprint = Blueprint("admin_blueprint" ,__name__)

@admin_blueprint.route("/admin")
def admin():
     return render_template("base_admin.html")



