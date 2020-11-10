from shop import db, login_manager
from datetime import datetime
from flask_login import UserMixin
import json


@login_manager.user_loader
def user_loader(user_id):
    return Register.query.get(user_id)

class Register(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50), unique=False)
    last_name = db.Column(db.String(50), unique=False)
    email = db.Column(db.String(50), unique=True)
    phone_number = db.Column(db.String(50), unique=True)
    gender = db.Column(db.String(5), unique=False)
    password = db.Column(db.String(200), unique=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    lock = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Register %r>' % self.username


class JsonEcodedDict(db.TypeDecorator):
    impl = db.Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)


class CustomerOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(20), default=None, nullable=True)
    address = db.Column(db.String(200), unique=False, nullable=True)
    customer_id = db.Column(db.Integer, unique=False, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    orders = db.Column(JsonEcodedDict)
    date_created = db.Column(db.DateTime, unique=False, nullable=True, default=datetime.utcnow)
    def __repr__(self):
        return '<CustomerOrder %r>' % self.invoice


db.create_all()
