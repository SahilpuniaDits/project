from flask_restful import Api
  
from services import buyers,seller



def initialize_routeapi(app):
    api = Api(app)
    api.add_resource(seller.register, '/api/register')
    api.add_resource(seller.LoginResource, '/api/login')
    api.add_resource(seller.landinfo, '/api/landinfo')
    api.add_resource(seller.PropertyQuote, '/api/property')
    api.add_resource(seller.SellerInfo, '/api/sellerinfo')
    api.add_resource(buyers.BuyerBudding, '/api/buyer')
    api.add_resource(buyers.getBid, '/api/getbid')