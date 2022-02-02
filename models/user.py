from models.db import db,migrate,ma
from flask import Flask
from passlib.apps import custom_app_context as pwd_context
from flask_migrate import Migrate
from sqlalchemy import ForeignKey


# app = Flask(__name__)
migrate = Migrate(db)

class User(db.Model):
    _tablename_ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(52), index=True)
    password_hash = db.Column(db.String(128))
    
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


class LendInformation(db.Model):
    __tablename__ = 'lendInfo'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(200))
    size = db.Column(db.String(100))
    
    seller_id = db.Column(db.Integer, ForeignKey('seller.id'))
    
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
    

    
class PropertyQuote(db.Model):
    __tablename__ = 'propertyQuote'
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer)
    quote = db.Column(db.Integer)
    
    lendInfo_id = db.Column(db.Integer, ForeignKey('lendInfo.id'))
   
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)


class SellerInformation(db.Model):
    __tablename__ = 'sellerInfo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    mobile = db.Column(db.String(13))
    
    seller_id = db.Column(db.Integer, ForeignKey('seller.id'))

    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
 

db.create_all()