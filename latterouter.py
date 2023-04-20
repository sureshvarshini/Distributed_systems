from flask import Flask
from database.models import db
from config import MARIA_ADDRESS
import os

# App instance
app = Flask(__name__)
print(MARIA_ADDRESS)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:pass@{MARIA_ADDRESS["maria_host"]}:{MARIA_ADDRESS["maria_port"]}/db'
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
    return os.environ.get("REGION") + " - Latte"
        
