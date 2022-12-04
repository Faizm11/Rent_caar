from extensions import db 

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(100), nullable=False)    

class Cars(db.Model):	
    __tablename__   = 'cars'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)      
    colour = db.Column(db.String(255), nullable=False) 
    price   = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))

class Type (db.Model):
    __tablename__ = "type" 
    id = db.Column(db.Integer,primary_key=True, autoincrement  = True) 
    name = db.Column(db.String(100), nullable=False)
    cars_id = db.Column(db.Integer, db.ForeignKey("cars.id"))