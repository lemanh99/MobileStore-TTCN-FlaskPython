from shop import db
from datetime import datetime
import json

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180),unique=False, nullable=False)
    profile = db.Column(db.String(180), unique=False, nullable=False,default='profile.jpg')

    def __repr__(self):
        return '<User %r>' % self.username

# class Register(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True)
#     first_name = db.Column(db.String(50), unique=False)
#     last_name = db.Column(db.String(50), unique=False)
#     email = db.Column(db.String(50), unique=True)
#     phone_number = db.Column(db.String(50), unique=True)
#     gender = db.Column(db.String(5), unique=False)
#     password = db.Column(db.String(200), unique=False)
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     lock = db.Column(db.Boolean, default=False)
#
#     def __repr__(self):
#         return '<Register %r>' % self.name

# class JsonEcodedDict(db.TypeDecorator):
#     impl = db.Text
#
#     def process_bind_param(self, value, dialect):
#         if value is None:
#             return '{}'
#         else:
#             return json.dumps(value)
#
#     def process_result_value(self, value, dialect):
#         if value is None:
#             return {}
#         else:
#             return json.loads(value)
#
# class CustomerOrder(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     invoice = db.Column(db.String(20), unique=True, nullable=False)
#     status = db.Column(db.String(20), default='Pending', nullable=False)
#     customer_id = db.Column(db.Integer, unique=False, nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     address = db.Column(db.String(500), nullable=True)
#     orders = db.Column(JsonEcodedDict)
#
#     def __repr__(self):
#         return '<CustomerOrder %r>' % self.invoice



db.create_all()