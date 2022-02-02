from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from flask_marshmallow import Marshmallow
import pymysql
from flask_migrate import Migrate

# app.config['SECRET_KEY'] = SECRET_KEY
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy()
migrate = Migrate(db)
# db.create_all()
ma = Marshmallow()