from models.db import db,SQLAlchemy
from flask import Flask
class Buyerbid(db.Model):
    __tablename__ = 'buyers'
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer)
    bid = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)

    def __init__(self,property_id,bid):
        self.property_id = property_id
        self.bid = bid

    def __repr__(self):
        record = {"property_id":self.property_id,"bid":self.bid}
        return record

    def serialize(self):
        return{"property_id":self.property_id,"bid":self.bid}

# db.create_all()
db.create_all()
       

 