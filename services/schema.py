# from Models.seller import LendInfo
from models.buyer import Buyerbid
from marshmallow import fields
from models.db import db,ma


class BuddingSchema(ma.Schema):
    class Meta:
       model = Buyerbid
       sqla_session = db.session

    id = fields.Number(dump_only=True)
    property_id = fields.Number(dump_only=True)
    bid = fields.Number(dump_only=True)