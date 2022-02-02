from flask_sqlalchemy import SQLAlchemy
from models.db import db
import models.user as reg
# import models.employee as emp
import datetime
import json

from flask import Flask, abort, jsonify, make_response, request, url_for
from flask_httpauth import HTTPBasicAuth
# from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
# from marshmallow import fields
from passlib.apps import custom_app_context as pwd_context
from models.user import LendInformation,SellerInformation,PropertyQuote
from models.buyer import Buyer
# from routes import initialize_routes
auth = HTTPBasicAuth()



class register(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        print(email, password, "<<<<<<<<<<<<<<<<<")
        if email is None or password is None:
            abort(400)  # missing arguments
            print(email, "**************")
        if reg.User.query.filter_by(email=email).first() is not None:
            abort(400)  # existing user
        user = reg.User(email=email)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'email': user.email}), 201


# @app.route('/api/login', methods=['POST'])
class login_user(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')

        user = reg.User.query.filter_by(email=email).first()

        passs = (pwd_context.verify(password, user.password_hash))

        if passs == True:

            return jsonify({'User': user.email, 'status': 'successfully logged In'}), 201,
        else:
            return jsonify({'status': 'Incorrect email or password'})

class landinfo(Resource):
    def post(self):
        address = request.json['address']
        size = request.json['size']
        
        land = LendInformation(address = address, size = size)
        db.session.add(land)
        db.session.commit()
        return jsonify({"status":"Successfully registered"})

# class LandListView(Resource):
#     def get(self):
#         land = LendInformation.query.all()
#         # landSchema = LandSchema(many = True)
#         landList = landSchema.dump(land)
        
#         return jsonify({"land list": landList})
class PropertyQuote(Resource):
    def post(self):
        property_id = request.json['property_id']
        quote = request.json['quote']
        
        property = PropertyQuote(property_id=property_id, quote=quote)
        db.session.add(property)
        db.session.commit()
        return jsonify({"status":"successfully registered"})

class SellerInfo(Resource):
    def post(self):
        name = request.json['name']
        email = request.json['email']
        mobile = request.json['mobile']
        
        seller = SellerInformation(name = name, email=email, mobile=mobile)
        db.session.add(seller)
        db.session.commit()
        return jsonify({"status":"Successfully registered"})

class BuyerBudding(Resource):
    def post(self):
        property_id = request.json['property_id']
        bid = request.json['bid']

        property = Buyer(property_id=property_id, bid=bid)
        db.session.add(property)
        db.session.commit()
        return jsonify({"status": "successfully registered"})