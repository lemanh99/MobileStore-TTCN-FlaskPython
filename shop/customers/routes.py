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
    # form = CustomerRegisterForm()
    # if form.validate_on_submit():
    #     hash_password = bcrypt.generate_password_hash(form.password.data)
    #     register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
    #     db.session.add(register)
    #     flash(f'Welcome {form.name.data} Thank you for registering', 'success')
    #     db.session.commit()
    #     return redirect(url_for('login'))
    # return render_template('customers/register.html', form=form)
    return render_template('customers/register.html')


@app.route('/login', methods=['GET', 'POST'])
def customer_login():
    # form = CustomerRegisterForm()
    # if form.validate_on_submit():
    #     hash_password = bcrypt.generate_password_hash(form.password.data)
    #     register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
    #     db.session.add(register)
    #     flash(f'Welcome {form.name.data} Thank you for registering', 'success')
    #     db.session.commit()
    #     return redirect(url_for('login'))
    # return render_template('customers/register.html', form=form)
    return render_template('customers/login.html')
