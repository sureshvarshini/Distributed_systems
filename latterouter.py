from flask import Flask
from database.models import db


# App instance
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@mariadb:3306/db'
from api import api
from cache.redis_cache import RedisClient
app.register_blueprint(api, url_prefix="/api")
# DB instance
db.init_app(app)
print("Connected to MARIADB")


with app.app_context():
    db.create_all()

print(app.url_map)

@app.route('/')
@app.route('/index')
def index():
    return "Latte"
        
