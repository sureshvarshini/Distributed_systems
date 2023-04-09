from flask import Flask
from database.models import db


# App instance
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pass@localhost:3001/db'
from api import api
app.register_blueprint(api, url_prefix="/api")
# DB instance
db.init_app(app)


with app.app_context():
    db.create_all()

print(app.url_map)
        
