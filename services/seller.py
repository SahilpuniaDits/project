import email
from flask_sqlalchemy import SQLAlchemy
from models.db import db
import models.users as reg
import datetime
import json
from models.users import User,Token
from flask import Flask, abort, jsonify, make_response, request, url_for,Response
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource
from passlib.apps import custom_app_context as pwd_context
from models.seller import LendInformation,SellerInformation,PropertyQuote
from models.buyer import Buyerbid
auth = HTTPBasicAuth()
from services.schema import BuddingSchema


class register(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        print(email, password, "<<<<<<<<<<<<<<<<<")
        if email is None or password is None:
            res = Response("email and password is null", status=400, mimetype='application/json')
            return res 
            # abort(400)  # missing arguments
            print(email, "**************")
        if reg.User.query.filter_by(email=email).first() is not None:
            resp = Response("email is already used", status=400, mimetype='application/json')
            return resp 
            # abort(400)  # existing user
        user = reg.User(email=email,password=password)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        # return jsonify({'email': user.email}), 201
        resp = Response("successfully register", status=201, mimetype='application/json')
        return resp 


# @app.route('/api/login', methods=['POST'])
# class login_user(Resource):
#     def post(self):
#         email = request.json.get('email')
#         password = request.json.get('password')

#         user = reg.User.query.filter_by(email=email).first()

#         passs = (pwd_context.verify(password, user.password_hash))

#         if passs == True:
#             # message = json.loads({"result": "created"})
#             resp = Response("successfully login", status=201, mimetype='application/json')
#             return resp #jsonify(result.data)
#             # return jsonify({'User': user.email, 'status': 'successfully logged In'}), 201,
#         else:
#             return jsonify({'status': 'Incorrect email or password'})

class LoginResource(Resource):
    def post(self):
        args = request.get_json()
        if 'email' in args and 'password' in args:
            user = User.query.filter_by(email=args['email']).first()
            if user is None:
                return {'message': "username or password is wrong"}, 404
            if user.password == args['password']:
                token = Token(user.id)
                db.session.add(token)
                db.session.commit()
                return {
                        "token": token.value
                    }
            else:
                return {'message': "username or password is wrong"}, 404
        else:
            return {
                    "must include both a username and password field", 400
                    }
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