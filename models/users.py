import email
from models.db import db,migrate,ma
from flask import Flask
from passlib.apps import custom_app_context as pwd_context
from uuid import uuid4


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    value = db.Column(db.String(170))

    def __init__(self,user_id):
        self.user_id = user_id
        self.value = str(uuid4())

    def serialize(self):
        return {
                "id": self.id,
                "user_id": self.user_id,
                "value": self.value,
                }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    # role_id = db.Column(db.Integer)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)


    def __init__(self, email, password):
        self.email = email
        self.password = password
        # self.role_id = role_id

    def serialize(self):
        return {
                "id": self.id,
                "email": self.email,
                "password": self.password,
                # "role_id": self.role_id
                }