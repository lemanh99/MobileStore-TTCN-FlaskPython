from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
import os
from flask_login import LoginManager
from flask_migrate import Migrate
import pyrebase



config = {
    "apiKey": "AIzaSyAbzMXHW-F63XzAJgqOIQxhfRJC_nP-iN0",
    "authDomain": "myshop-dc0d3.firebaseapp.com",
    "storageBucket": "myshop-dc0d3.appspot.com",
    "databaseURL": "https://myshop-dc0d3.firebaseapp.com/",
    "projectId": "myshop-dc0d3",
    "messagingSenderId": "1090563198053",
    "appId": "1:1090563198053:web:42f96da321a4d4a0d5ca8c",
    "measurementId": "G-D8R8PB4T3H"
}
#
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# get_all_products()

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/myshop4'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:YKVlfd89801@node238154-laptrinh.j.layershift.co.uk:80/myshop4'
DB_URL = 'postgresql+psycopg2://lmzmukpyharrik:a334089832744e3280289b61f1c3dc821407562c6ff6bc6d87638453b43f04cf@ec2-35-175-155-248.compute-1.amazonaws.com:5432/da2984f8vfjrpm'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SECRET_KEY'] = 'hfouewhfoiwefoquw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

migrate = Migrate(app, db)
with app.app_context():
    if db.engine.url.drivername == "mysql":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'customer_login'
login_manager.needs_refresh_message_category = 'danger'
login_manager.login_message = "Please login first"

from shop.admin import routes
from shop.products import routes
from shop.carts import routes
from shop.customers import routes

