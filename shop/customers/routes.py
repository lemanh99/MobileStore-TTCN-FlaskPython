from flask import render_template, session, request, redirect, url_for, flash, current_app, make_response
from flask_login import login_required, current_user, logout_user, login_user
from shop import app, db, photos, bcrypt
from .forms import CustomerRegisterForm, CustomerLoginFrom
from .models import Register, CustomerOrder
import secrets
import os
import json


# import pdfkit
# import stripe

@app.route('/register', methods=['GET', 'POST'])
def customer_register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = CustomerRegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(username=form.username.data, email=form.email.data, first_name=form.first_name.data,
                            last_name=form.last_name.data, phone_number=form.phone_number.data, gender=form.gender.data,
                            password=hash_password)
        db.session.add(register)
        flash(f'Welcome {form.first_name.data} {form.last_name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('customer_login'))
    return render_template('customers/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def customer_login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(username=form.username.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next = request.args.get('next')
            return redirect(next or url_for('home'))
        flash('Incorrect email and password', 'danger')
        return redirect(url_for('customer_login'))
    return render_template('customers/login.html', form=form)


@app.route('/logout')
@login_required
def customer_logout():
    if not current_user.is_authenticated:
        return redirect(url_for('home'))
    logout_user()
    return redirect(url_for('home'))
