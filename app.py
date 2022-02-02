from flask import Flask
from routes import initialize_routeapi
from models.db import db,SQLAlchemy,Migrate
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/apis'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
migrate = Migrate(db)
db.init_app(app)

initialize_routeapi(app)
# with app.app_context():
#     db.create_all()
if __name__ == '__main__':
    app.run(debug=True)

