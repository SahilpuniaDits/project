from models.db import db
# from passlib.apps import custom_app_context as pwd_context



class Buyer(db.Model):
    __tablename__ = 'buyers'
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer)
    bid = db.Column(db.Integer)
    


db.create_all()