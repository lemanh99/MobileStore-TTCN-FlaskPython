from shop import db
from datetime import datetime
from shop.customers.models import Register


class Addproduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    brand = db.relationship('Brand', backref=db.backref('brands', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')

    def __repr__(self):
        return '<Addproduct %r>' % self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

    def __repr__(self):
        return '<Category %r>' % self.name


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    category = db.relationship('Category', backref=db.backref('category', lazy=True))
    name = db.Column(db.String(30), nullable=False, unique=False)

    def __repr__(self):
        return '<Brand %r>' % self.name


class Rate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('addproduct.id'), nullable=False)
    product = db.relationship('Addproduct', backref=db.backref('addproducts', lazy=True))

    register_id = db.Column(db.Integer, db.ForeignKey('register.id'), nullable=False)
    register = db.relationship('Register', backref=db.backref('registers', lazy=True))

    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    desc = db.Column(db.Text, nullable=False)
    rate_number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Rate %r>' % self.product_id


db.create_all()
