from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import pymysql
from flask_uploads import IMAGES, UploadSet,configure_uploads,patch_request_class
import os
pymysql.install_as_MySQLdb()


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:060599@localhost:3306/shop'
app.config['SECRET_KEY']='hfouewhfoiwefoquw'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST']=os.path.join(basedir, 'static/images')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

db = SQLAlchemy(app)
bcrypt =Bcrypt(app)

from shop.admin import routes
from shop.products import routes