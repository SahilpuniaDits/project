from models.db import app
from venv import create
from flask import Flask
from routes import initialize_routeapi
from models.db import db,SQLAlchemy,Migrate
from flask_migrate import Migrate
from models.buyer import Buyerbid
import sqlite3

con = sqlite3.connect("Buy_sell.db")
print("Database opened successfully")
con.close()
# db.create_all()
# db.session.commit()
   
initialize_routeapi(app)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    

