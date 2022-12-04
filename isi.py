from models.mobil import *
from extensions import db 
from app import app
app.app_context().push()

c1= Category()
c2= Category()
c3 = Category()
c4= Category()
c5= Category()
c6 = Category()
c7 = Category()
c1.name = "SUV"
c2.name = "Sedan"
c3.name = "MPV"
c4.name = "Hatcback"
c5.name = "Commercial" 
c6.name = "Sport" 
c7.name = "Hybrid" 

db.session.add_all([c1,c2,c3,c4,c5,c6,c7])
db.session.commit()