from flask import render_template, session, redirect, request, url_for, flash,session

from shop import app, db, bcrypt
from .form import RegistrationForm, LoginForm
from .models import Admin
from shop.products.models import Addproduct,Brand,Category

@app.route('/admin')
def admin():
    if 'email'not in session:
        flash(f'please login first','danger')
        return redirect(url_for('login'))
    user = Admin.query.filter_by(email=session['email']).all()

    return render_template('test/index2.html', title='Admin page' , user=user[0])

@app.route('/admin_manager')
def admin_manager():
    if 'email'not in session:
        flash(f'please login first','danger')
        return redirect(url_for('login'))
    user = Admin.query.filter_by(email=session['email']).all()
    admins =Admin.query.all()
    return render_template('admin/admin-manager.html', title='All admin page' , user=user[0], admins=admins)

@app.route('/delete_admin/<int:id>', methods=['GET','POST'])
def delete_admin(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    admin = Admin.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(admin)
        db.session.commit()
        flash(f"The brand {admin.name} was deleted from your database","success")
        return redirect(url_for('admin_manager'))
    flash(f"The brand {admin.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin_manager'))


@app.route('/product')
def product():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    products = Addproduct.query.all()
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('admin/index.html', title='Product page',products=products, user=user[0])

@app.route('/brands')
def brands():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.order_by(Brand.id.desc()).all()
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('admin/brand.html', title='brands',brands=brands, user=user[0])


@app.route('/categories')
def categories():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    categories = Category.query.order_by(Category.id.desc()).all()
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('admin/brand.html', title='categories',categories=categories, user=user[0])


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'email'not in session:
        flash(f'please login first','danger')
        return redirect(url_for('login'))
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = Admin(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f' Wellcom {form.name.data} Thanks for registering', 'success')
        return redirect(url_for('register'))
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('admin/register.html', form=form, title='Registration page', user=user[0])

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Admin.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'welcome {form.email.data} you are logedin now','success')
            return redirect(url_for('admin'))
        else:
            flash(f'Wrong email and password', 'danger')
            return redirect(url_for('login'))
    return render_template('admin/login.html',title='Login page',form=form)
