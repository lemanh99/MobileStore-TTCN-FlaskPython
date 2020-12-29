import os
import urllib
from itertools import product

from flask import render_template, session, redirect, request, url_for, flash, session, current_app
from shop import app, db, bcrypt, storage
from .form import RegistrationForm, LoginForm, CustomerRegisterForm
from .models import Admin
from shop.customers.models import Register, CustomerOrder
from shop.products.models import Addproduct, Brand, Category, Rate


def synchronization():
    try:
        urllib.request.urlopen("https://console.firebase.google.com/")  # Python 3.x
        ls = ['background.png', 'Assets.png', 'bg.jpg', 'AdminLTELogo.png']
        for i in ls:
            if not os.path.isfile(os.path.join(current_app.root_path, "static/images/" + i)):
                storage.child("images/" + i).download(
                    os.path.join(current_app.root_path, "static/images/" + i))
        products = Addproduct.query.all();
        for product in products:
            if not os.path.isfile(os.path.join(current_app.root_path, "static/images/" + product.image_1)):
                storage.child("images/" + product.image_1).download(
                    os.path.join(current_app.root_path, "static/images/" + product.image_1))
            if not os.path.isfile(os.path.join(current_app.root_path, "static/images/" + product.image_2)):
                storage.child("images/" + product.image_2).download(
                    os.path.join(current_app.root_path, "static/images/" + product.image_2))
            if not os.path.isfile(os.path.join(current_app.root_path, "static/images/" + product.image_3)):
                storage.child("images/" + product.image_3).download(
                    os.path.join(current_app.root_path, "static/images/" + product.image_3))
        return True
    except:
        return False


@app.route('/synchronization')
def data_syn():
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    if synchronization():
        flash(f'Synchronization Data Success', 'success')
        return redirect(url_for('admin_manager'))
    else:
        flash(f'Synchronization Data Failure, Please Reconnect Internet', 'danger')
        return redirect(url_for('admin_manager'))


@app.route('/admin/customer_register', methods=['GET', 'POST'])
def admin_register_custormer():
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    form = CustomerRegisterForm()
    if form.validate_on_submit():
        if Admin.query.filter_by(email=form.email.data).first():
            flash(f'Email Used!', 'danger')
            return redirect(url_for('admin_register_custormer'))
        if Register.query.filter_by(email=form.email.data).first():
            flash(f'Email Used!', 'danger')
            return redirect(url_for('admin_register_custormer'))
        if Register.query.filter_by(phone_number=form.phone_number.data).first():
            flash(f'Phone Number Used!', 'danger')
            return redirect(url_for('admin_register_custormer'))
        try:
            hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')
            register = Register(username=form.username.data, email=form.email.data, first_name=form.first_name.data,
                                last_name=form.last_name.data, phone_number=form.phone_number.data,
                                gender=form.gender.data,
                                password=hash_password)
            db.session.add(register)
            flash(f'Register account " {form.first_name.data} {form.last_name.data} " success', 'success')
            db.session.commit()
            return redirect(url_for('admin_register_custormer'))
        except:
            flash(f'Error!', 'danger')
            return redirect(url_for('admin_register_custormer'))
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('admin/customer_register.html', form=form, user=user[0])


@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    return redirect(url_for('admin_manager'))


@app.route('/admin_manager')
def admin_manager():
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    user = Admin.query.filter_by(email=session['email']).all()
    admins = Admin.query.all()
    return render_template('admin/admin-manager.html', title='Admin manager page', user=user[0], admins=admins)


@app.route('/customer_manager')
def customer_manager():
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    user = Admin.query.filter_by(email=session['email']).all()
    customers = Register.query.all()
    return render_template('admin/customer_manager.html', title='Customer manager page', user=user[0],
                           customers=customers)


@app.route('/admin/orders')
def orders_manager():
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    # page = request.args.get('page', 1, type=int)
    user = Admin.query.filter_by(email=session['email']).all()
    customers = Register.query.all()
    # products = Addproduct.query.order_by(Addproduct.id.desc())
    # orders = CustomerOrder.query.filter(CustomerOrder.status != None).filter(
    #     CustomerOrder.status != "Cancelled").order_by(CustomerOrder.id.desc()).paginate(page=page, per_page=10)\

    orders = CustomerOrder.query.filter(CustomerOrder.status != None).order_by(CustomerOrder.id.desc()).all()
    return render_template('admin/manage_orders.html', title='Order manager page', user=user[0], orders=orders,
                           customers=customers)


@app.route('/accept_order/<int:id>', methods=['GET', 'POST'])
def accept_order(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    customer_order = CustomerOrder.query.get_or_404(id)
    for key, product in customer_order.orders.items():
        if request.method == "POST":
            product_order = Addproduct.query.get_or_404(key)
            if (product_order.stock - int(product['quantity'])) >= 0:
                product_order.stock -= int(product['quantity'])
                db.session.commit()
                customer_order.status = 'Accepted'
                db.session.commit()
            else:
                flash('Quantity in stock has been exhausted', 'danger')
            return redirect(url_for('orders_manager'))
    return redirect(url_for('orders_manager'))


@app.route('/delete_order/<int:id>', methods=['GET', 'POST'])
def delete_order(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    customer = CustomerOrder.query.get_or_404(id)
    if request.method == "POST":
        customer.status = "Cancelled"
        db.session.commit()
        return redirect(url_for('orders_manager'))
    return redirect(url_for('orders_manager'))


@app.route('/lock_customer/<int:id>', methods=['GET', 'POST'])
def lock_customer(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    customer = Register.query.get_or_404(id)
    if request.method == "POST":
        customer.lock = 1
        db.session.commit()
        return redirect(url_for('customer_manager'))
    return redirect(url_for('customer_manager'))


@app.route('/unlock_customer/<int:id>', methods=['GET', 'POST'])
def unlock_customer(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    customer = Register.query.get_or_404(id)
    if request.method == "POST":
        customer.lock = 0
        db.session.commit()
        return redirect(url_for('customer_manager'))
    return redirect(url_for('customer_manager'))


@app.route('/delete_customer/<int:id>', methods=['GET', 'POST'])
def delete_customer(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    customer = Register.query.get_or_404(id)
    if request.method == "POST":
        rates = Rate.query.filter(Rate.register_id == id).all()
        for rate in rates:
            db.session.delete(rate)
            db.session.commit()
        db.session.delete(customer)
        db.session.commit()
        flash(f"The customer {customer.username} was deleted from your database", "success")
        return redirect(url_for('customer_manager'))
    flash(f"The customer {customer.username} can't be  deleted from your database", "warning")
    return redirect(url_for('customer_manager'))


@app.route('/delete_admin/<int:id>', methods=['GET', 'POST'])
def delete_admin(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    admin = Admin.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(admin)
        db.session.commit()
        flash(f"The admin {admin.name} was deleted from your database", "success")
        return redirect(url_for('admin_manager'))
    flash(f"The admin {admin.name} can't be  deleted from your database", "warning")
    return redirect(url_for('admin_manager'))


@app.route('/product')
def product():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    # products = Addproduct.query.all()
    # page = request.args.get('page', 1, type=int)
    # products = Addproduct.query.order_by(Addproduct.id.desc()).paginate(page=page, per_page=10)
    products = Addproduct.query.all()
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('admin/index.html', title='Product page', products=products, user=user[0])


@app.route('/brands')
def brands():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))

    brands = Brand.query.join(Category).add_columns(Category.name).filter(Brand.category_id == Category.id).order_by(
        Brand.id.desc()).all()
    print(brands)
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('admin/manage_brand.html', title='brands', brands=brands, user=user[0])


@app.route('/categories')
def categories():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    categories = Category.query.order_by(Category.id.desc()).all()
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('admin/manage_brand.html', title='categories', categories=categories, user=user[0])


@app.route('/admin/changepassword', methods=['GET', 'POST'])
def changes_password():
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    user = Admin.query.filter_by(email=session['email'])
    detail_password_admin = Admin.query.get_or_404(user[0].id)
    old_password = request.form.get('oldpassword')
    new_password = request.form.get('newpassword')
    if request.method == "POST":
        if not bcrypt.check_password_hash(detail_password_admin.password, old_password.encode('utf8')):
            flash(f'Old passwords do not match!', 'danger')
            return redirect(url_for('changes_password'))
        detail_password_admin.password = bcrypt.generate_password_hash(new_password).decode('utf8')
        flash(f'Change Password Complete!', 'success')
        db.session.commit()
        return redirect(url_for('changes_password'))
    return render_template('admin/change_password.html', title='Change Password', user=user[0])


@app.route('/admin/register', methods=['GET', 'POST'])
def register():
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')
        user = Admin(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f' Wellcom {form.name.data} Thanks for registering', 'success')
        return redirect(url_for('register'))
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('admin/admin_register.html', form=form, title='Registration page', user=user[0])


@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Admin.query.filter_by(email=form.email.data).first()
        password = form.password.data.encode('utf8')
        if user and bcrypt.check_password_hash(user.password, password):
            session['email'] = form.email.data
            flash(f'welcome {form.email.data} you are logedin now', 'success')
            return redirect(url_for('admin'))
        else:
            flash(f'Wrong email and password', 'danger')
            return redirect(url_for('login'))
    return render_template('admin/login.html', title='Login page', form=form)


@app.route('/admin/logout')
def logout():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
    else:
        session.pop('email', None)
    return redirect(url_for('login'))
