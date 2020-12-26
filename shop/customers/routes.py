from flask import render_template, session, request, redirect, url_for, flash, current_app, make_response
from flask_login import login_required, current_user, logout_user, login_user
from shop import app, db, photos, bcrypt
from .forms import CustomerRegisterForm, CustomerLoginFrom
from .models import Register, CustomerOrder
from shop.products.models import Category, Brand, Addproduct
from shop.carts.routes import clearcart, MagerDicts
from flask import Markup
import secrets
import os
import json

# import pdfkit
# import stripe
from shop.admin.models import Admin


def brands():
    # brands = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    brands = Brand.query.all()
    return brands


def categories():
    # categories = Category.query.join(Addproduct, (Category.id == Addproduct.category_id)).all()
    categories = Category.query.order_by(Category.name.desc()).all()
    return categories


@app.route('/myaccount', methods=['GET', 'POST'])
@login_required
def update_account():
    detail_customer = Register.query.get_or_404(current_user.id)
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    email = request.form.get('email')
    phone_number = request.form.get('phone')
    gender = request.form.get('gender')
    if request.method == "POST":
        if detail_customer.email != email:
            if Register.query.filter_by(email=email).first():
                flash(f'Email Used!', 'danger')
                return redirect(url_for('update_account'))
        if detail_customer.phone_number != phone_number:
            if Register.query.filter_by(phone_number=phone_number).first():
                flash(f'Phone Number Used!', 'danger')
                return redirect(url_for('update_account'))
        detail_customer.first_name = first_name
        detail_customer.last_name = last_name
        detail_customer.email = email
        detail_customer.phone_number = phone_number
        detail_customer.gender = gender
        flash(f'Information change complete!', 'success')
        db.session.commit()
        return redirect(url_for('update_account'))
    return render_template('customers/myaccount.html', detail_customer=detail_customer, brands=brands(),
                           categories=categories())


@app.route('/changepassword', methods=['GET', 'POST'])
@login_required
def change_password():
    detail_password_customer = Register.query.get_or_404(current_user.id)
    old_password = request.form.get('oldpassword')
    new_password = request.form.get('newpassword')
    if request.method == "POST":
        if not bcrypt.check_password_hash(detail_password_customer.password, old_password.encode('utf8')):
            flash(f'Old passwords do not match!', 'danger')
            return redirect(url_for('change_password'))

        detail_password_customer.password = bcrypt.generate_password_hash(new_password).decode('utf8')
        flash(f'Change Password Complete!', 'success')
        db.session.commit()
        return redirect(url_for('change_password'))
    return render_template('customers/myaccount.html', detail_password_customer=detail_password_customer,
                           brands=brands(),
                           categories=categories())


@app.route('/register', methods=['GET', 'POST'])
def customer_register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = CustomerRegisterForm()
    if form.validate_on_submit():
        if Admin.query.filter_by(email=form.email.data).first():
            flash(f'Email Used!', 'danger')
            return redirect(url_for('customer_register'))
        if Register.query.filter_by(email=form.email.data).first():
            flash(f'Email Used!', 'danger')
            return redirect(url_for('customer_register'))
        if Register.query.filter_by(phone_number=form.phone_number.data).first():
            flash(f'Phone Number Used!', 'danger')
            return redirect(url_for('customer_register'))
        try:
            hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')
            register = Register(username=form.username.data, email=form.email.data, first_name=form.first_name.data,
                                last_name=form.last_name.data, phone_number=form.phone_number.data,
                                gender=form.gender.data,
                                password=hash_password)
            db.session.add(register)
            flash(f'Welcome {form.first_name.data} {form.last_name.data} Thank you for registering', 'success')
            db.session.commit()
        except:
            flash(f'Error!', 'danger')
            return redirect(url_for('customer_register'))

        return redirect(url_for('customer_login'))
    return render_template('customers/register.html', form=form, brands=brands(), categories=categories())


@app.route('/login', methods=['GET', 'POST'])
def customer_login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        # Register.query.filter_by(lock=False).first()
        user = Register.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data.encode('utf8')):
            if user.lock == True:
                flash(Markup(
                    "Account has been locked ! <a href='mailto: lemanh@gmail.com' class='alert-link' >Help here</a>"),
                    'danger')
                return redirect(url_for('customer_login'))
            login_user(user)

            # Xu ly gio hang
            if 'Shoppingcart' in session:
                orders = CustomerOrder.query.filter(CustomerOrder.customer_id == current_user.id).filter(
                    CustomerOrder.status == None).order_by(CustomerOrder.id.desc()).all()
                product_id = [order.orders for order in orders]
                for key, item in session['Shoppingcart'].items():
                    if key not in product_id:
                        customer_id = current_user.id
                        invoice = secrets.token_hex(5)
                        order = CustomerOrder(invoice=invoice, customer_id=customer_id,
                                              orders={key: session['Shoppingcart'][key]},
                                              status=None)
                        db.session.add(order)
                        db.session.commit()
            session.pop('Shoppingcart', None)
            orders = CustomerOrder.query.filter(CustomerOrder.customer_id == current_user.id).filter(
                CustomerOrder.status == None).order_by(CustomerOrder.id.desc()).all()
            session.modified = True
            for order in orders:
                for product_id, DictItems in order.orders.items():
                    DictItems = {product_id: DictItems}
                    if 'Shoppingcart' not in session:
                        session['Shoppingcart'] = DictItems
                    else:
                        session['Shoppingcart'] = MagerDicts(session['Shoppingcart'], DictItems)

            next = request.args.get('next')
            return redirect(next or url_for('home'))
        flash('Incorrect email and password', 'danger')
        return redirect(url_for('customer_login'))
    return render_template('customers/login.html', form=form, brands=brands(), categories=categories())


@app.route('/login/<string:page>_<int:id>', methods=['GET', 'POST'])
def customer_login_page(page, id):
    if current_user.is_authenticated:
        if page == "rate":
            return redirect(url_for('detail', id))
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data.encode('utf8')):
            login_user(user)
            return redirect(url_for('detail', id=id))
        flash('Incorrect email and password', 'danger')
        return redirect(url_for('customer_login_page', page=page, id=id))
    return render_template('customers/login.html', form=form, brands=brands(), categories=categories())


@app.route('/logout')
@login_required
def customer_logout():
    if not current_user.is_authenticated:
        return redirect(url_for('home'))
    logout_user()
    clearcart()
    return redirect(url_for('home'))


@app.route('/getorder/')
@login_required
def get_order():
    if not current_user.is_authenticated:
        return redirect(url_for('customer_login'))
    customer_id = current_user.id
    customer = Register.query.filter_by(id=customer_id).first()
    orders = CustomerOrder.query.filter(
        CustomerOrder.customer_id == current_user.id).filter(
        CustomerOrder.status == None).order_by(CustomerOrder.id.desc()).all()
    invoices = [order.invoice for order in orders]
    orders = []
    for invoice in invoices:
        order = CustomerOrder.query.filter_by(customer_id=customer_id, invoice=invoice).order_by(
            CustomerOrder.id.desc()).first()
        orders.append(order)
    subtotals = 0
    discounttotal = 0
    for key, product in session['Shoppingcart'].items():
        discounttotal += float(product['discount'] / 100) * float(product['price']) * int(product['quantity'])
        subtotals += float(product['price']) * int(product['quantity'])
    subtotals -= discounttotal
    return render_template('customers/order.html', invoices=invoices, subtotals=subtotals, customer=customer,
                           orders=orders, brands=brands(), categories=categories())


@app.route('/submit_order', methods=['POST'])
@login_required
def submit_order():
    address = request.form.get('CustomerAddress')
    invoice_customer = request.form.get('invoice_customer')
    if request.method == "POST":
        for invoice in invoice_customer.split(','):
            customer_order = CustomerOrder.query.filter_by(invoice=invoice).first()
            detail_order = CustomerOrder.query.get_or_404(customer_order.id)
            detail_order.status = "Pending"
            detail_order.address = address
            db.session.commit()
        clearcart()
    return redirect(url_for('payment_history'))


@app.route('/payment_history')
@login_required
def payment_history():
    orders = CustomerOrder.query.filter(CustomerOrder.customer_id == current_user.id).filter(
        CustomerOrder.status != None).order_by(CustomerOrder.id.desc()).all()
    return render_template('customers/myaccount.html', orders=orders, brands=brands(), categories=categories())
