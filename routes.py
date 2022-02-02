from flask_restful import Api
  
from services.apis import register,login_user,landinfo,PropertyQuote,SellerInfo,BuyerBudding


def initialize_routeapi(app):
    api = Api(app)
    api.add_resource(register, '/api/register')
    api.add_resource(login_user, '/api/login')
    api.add_resource(landinfo, '/api/landinfo')
    api.add_resource(PropertyQuote, '/api/property')
    api.add_resource(SellerInfo, '/api/sellerinfo')
    api.add_resource(BuyerBudding, '/api/buyer')