from models.db import db
import models.seller as reg
import datetime
import json

from flask import Flask, abort, jsonify, make_response, request, url_for,Response
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource
from passlib.apps import custom_app_context as pwd_context
from models.seller import LendInformation,SellerInformation,PropertyQuote
from models.buyer import Buyerbid
auth = HTTPBasicAuth()
from services.schema import BuddingSchema



class BuyerBudding(Resource):
    def post(self):
        property_id = request.json['property_id']
        bid = request.json['bid']

        property = Buyerbid(property_id=property_id, bid=bid)
        db.session.add(property)
        db.session.commit()
        return jsonify({"status": "successfully registered"})


class getBid(Resource):    
    def get(self):        
        bid = Buyerbid.query.filter_by()
        
        # max_bid = db.session.query(func.max(BuyerBudding.bid)).scalar()
        # bid = db.session.query(BuyerBudding).filter(BuyerBudding.bid == max_bid).all()
        
        buddingSchema = BuddingSchema(many=True)
        buddingList = buddingSchema.dump(bid)


        return jsonify({"Bid list": buddingList})    