import secrets

from flask import render_template, session, request, redirect, url_for, flash, current_app
from flask_login import current_user

from shop import db, app
from shop.customers.models import CustomerOrder
from shop.products.models import Category, Brand, Addproduct
from shop.products.routes import brands, categories
import json


def brands():
    # brands = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    brands = Brand.query.all()
    return brands


def categories():
    # categories = Category.query.join(Addproduct, (Category.id == Addproduct.category_id)).all()
    categories = Category.query.order_by(Category.name.desc()).all()
    return categories


def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))


@app.route('/addcart', methods=['POST'])
def AddCart():
    try:
        product_id = request.form.get('product_id')
        quantity = int(request.form.get('quantity'))
        color = request.form.get('colors')
        product = Addproduct.query.filter_by(id=product_id).first()
        brand = Brand.query.filter_by(id=product.brand_id).first().name
        if request.method == "POST":
            # if product_id in orders
            DictItems = {product_id: {'name': product.name, 'price': float(product.price), 'discount': product.discount,
                                      'color': color, 'quantity': quantity, 'image': product.image_1,
                                      'colors': product.colors, 'brand': brand}}
            if 'Shoppingcart' in session:
                # print(session['Shoppingcart'])
                if product_id in session['Shoppingcart']:
                    for key, item in session['Shoppingcart'].items():
                        if int(key) == int(product_id):
                            session.modified = True
                            item['quantity'] += quantity;
                            if current_user.is_authenticated:
                                orders = CustomerOrder.query.filter(
                                    CustomerOrder.customer_id == current_user.id).filter(
                                    CustomerOrder.status == None).order_by(CustomerOrder.id.desc()).all()
                                for order in orders:
                                    if product_id in order.orders:
                                        customer_order = CustomerOrder.query.get_or_404(order.id)
                                        customer_order.orders = {product_id: session['Shoppingcart'][product_id]}
                                        db.session.commit()
                else:
                    session['Shoppingcart'] = MagerDicts(session['Shoppingcart'], DictItems)
                    if current_user.is_authenticated:
                        customer_id = current_user.id
                        invoice = secrets.token_hex(5)
                        order = CustomerOrder(invoice=invoice, customer_id=customer_id,
                                              orders={product_id: session['Shoppingcart'][product_id]},
                                              status=None)
                        db.session.add(order)
                        db.session.commit()
                    return redirect(request.referrer)
            else:
                session['Shoppingcart'] = DictItems
                if current_user.is_authenticated:
                    customer_id = current_user.id
                    invoice = secrets.token_hex(5)
                    order = CustomerOrder(invoice=invoice, customer_id=customer_id,
                                          orders={product_id: session['Shoppingcart'][product_id]},
                                          status=None)
                    db.session.add(order)
                    db.session.commit()

                return redirect(request.referrer)

    except Exception as e:
        print("Loi", e)
    finally:
        return redirect(request.referrer)


@app.route('/carts')
def getCart():
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return render_template('products/carts.html', empty=True, brands=brands(),
                               categories=categories())
    subtotals = 0
    discounttotal = 0
    for key, product in session['Shoppingcart'].items():
        discounttotal += (product['discount'] / 100) * float(product['price']) * int(product['quantity'])
        subtotals += float(product['price']) * int(product['quantity'])
    return render_template('products/carts.html', discounttotal=discounttotal, subtotals=subtotals, brands=brands(),
                           categories=categories())
    # return render_template('products/carts.html', brands=brands(), categories=categories())


@app.route('/updatecart/<int:code>', methods=['POST'])
def updatecart(code):
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('getCart'))
    if request.method == "POST":
        quantity = request.form.get('quantity')
        color = request.form.get('color')
        try:
            session.modified = True
            for key, item in session['Shoppingcart'].items():
                if int(key) == code:
                    item['quantity'] = quantity
                    item['color'] = color
                    if current_user.is_authenticated:
                        orders = CustomerOrder.query.filter(
                            CustomerOrder.customer_id == current_user.id).filter(
                            CustomerOrder.status == None).order_by(CustomerOrder.id.desc()).all()
                        for order in orders:
                            if key in order.orders:
                                customer_order = CustomerOrder.query.get_or_404(order.id)
                                customer_order.orders = {key: session['Shoppingcart'][key]}
                                db.session.commit()
                    return redirect(url_for('getCart'))
        except Exception as e:
            print(e)
            return redirect(url_for('getCart'))


@app.route('/deleteitem/<int:id>')
def deleteitem(id):
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('getCart'))
    try:
        orders = CustomerOrder.query.filter(
            CustomerOrder.customer_id == current_user.id).filter(
            CustomerOrder.status == None).all()
        for order in orders:
            for key, item in order.orders.items():
                if int(key) == id:
                    customer = CustomerOrder.query.get_or_404(order.id)
                    db.session.delete(customer)
                    db.session.commit()
                    break
        session.modified = True
        for key, item in session['Shoppingcart'].items():
            if int(key) == id:
                session['Shoppingcart'].pop(key, None)
                return redirect(url_for('getCart'))
    except Exception as e:
        print(e)
        return redirect(url_for('getCart'))


@app.route('/clearcart')
def clearcart():
    try:
        session.pop('Shoppingcart', None)
        if current_user.is_authenticated:
            orders = CustomerOrder.query.filter(CustomerOrder.customer_id == current_user.id).filter(
                CustomerOrder.status == None).order_by(CustomerOrder.id.desc()).all()
            for order in orders:
                db.session.delete(order)
                db.session.commit()
        return redirect(url_for('getCart'))
    except Exception as e:
        print(e)
