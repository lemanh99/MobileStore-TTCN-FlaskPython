import urllib

from flask import render_template, session, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user, logout_user, login_user
from shop import app, db, photos, storage
from .models import Category, Brand, Addproduct, Rate, Register
from .forms import Addproducts, Rates
from shop.admin.models import Admin
import secrets
import os


def brands():
    # brands = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    brands = Brand.query.all()
    return brands


def categories():
    # categories = Category.query.join(Addproduct, (Category.id == Addproduct.category_id)).all()
    categories = Category.query.order_by(Category.name.desc()).all()
    return categories


def registers():
    registers = Register.query.join(Rate, (Register.id == Rate.register_id)).all()
    return registers


def medium():
    products = Addproduct.query.filter(Addproduct.stock > 0).all()
    dst = {}
    for product in products:
        rates = Rate.query.filter(Rate.product_id == product.id).all()
        lenght = len(rates)
        if lenght == 0:
            average = 5
        else:
            sum_value = sum([rate.rate_number for rate in rates])
            average = sum_value / lenght
        dst[product.id] = [average, lenght]
    return dst


@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    category = Category.query.filter_by(name="Smartphone").first()
    products_all = Addproduct.query.filter(Addproduct.stock > 0).filter(Addproduct.category_id == category.id).order_by(
        Addproduct.id.desc()).paginate(page=page,
                                       per_page=4)
    products_hot = Addproduct.query.filter(Addproduct.stock > 0).filter(Addproduct.category_id == category.id).order_by(
        Addproduct.price.desc()).limit(3).all()
    products_new = Addproduct.query.filter(Addproduct.stock > 0).filter(Addproduct.category_id == category.id).order_by(
        Addproduct.id.desc()).all()
    products_sell = Addproduct.query.filter(Addproduct.stock > 0).filter(
        Addproduct.category_id == category.id).order_by(Addproduct.discount.desc()).limit(10).all()
    products = {'all': products_all, 'hot': products_hot, 'new': products_new, 'sell': products_sell,
                'average': medium()}
    return render_template('customers/index.html', products=products, brands=brands(), categories=categories())


@app.route('/category')
def get_all_category():
    page = request.args.get('page', 1, type=int)
    products_all = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).paginate(page=page,
                                                                                                         per_page=9)
    products_new = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).limit(2).all()
    products = {'all': products_all, 'new': products_new, 'average': medium()}
    return render_template('products/category.html', products=products, brands=brands(), categories=categories())


@app.route('/category/brand/<string:name>')
def get_brand(name):
    page = request.args.get('page', 1, type=int)
    get_brand = Brand.query.filter_by(name=name).first_or_404()
    brand = Addproduct.query.filter_by(brand=get_brand).paginate(page=page, per_page=9)

    products_new = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).limit(2).all()
    products = {'all': brand, 'new': products_new, 'average': medium()}
    return render_template('products/category.html', products=products, brand=name, brands=brands(),
                           categories=categories(),
                           get_brand=get_brand)


@app.route('/categories/<string:name>')
def get_category(name):
    page = request.args.get('page', 1, type=int)
    get_cat = Category.query.filter_by(name=name).first_or_404()
    get_cat_prod = Addproduct.query.filter_by(category=get_cat).paginate(page=page, per_page=9)
    products_new = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).limit(2).all()
    products = {'all': get_cat_prod, 'new': products_new, 'average': medium()}
    get_cat_prod = {'name': name, 'id': get_cat.id}
    return render_template('products/category.html', products=products, get_cat_prod=get_cat_prod, brands=brands(),
                           categories=categories(),
                           get_cat=get_cat)


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getbrand = request.form.get('brand')
        category = request.form.get('category')
        brand = Brand(name=getbrand, category_id=category)

        db.session.add(brand)
        flash(f'The brand {getbrand} was added to your database', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    user = Admin.query.filter_by(email=session['email']).all()
    categories = Category.query.all()
    return render_template('products/addbrand.html', title='Add brand', categories=categories, brands='brands',
                           user=user[0])


@app.route('/updatebrand/<int:id>', methods=['GET', 'POST'])
def updatebrand(id):
    if 'email' not in session:
        flash('Login first please', 'danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method == "POST":
        print("Brand", brand)
        updatebrand.name = brand
        flash(f'The brand {updatebrand.name} was updated', 'success')
        db.session.commit()
        return redirect(url_for('brands'))
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('products/updatebrand.html', title='Uppdate brand', brands='brands', updatebrand=updatebrand,
                           categories=categories(), user=user[0])


@app.route('/deletebrand/<int:id>', methods=['GET', 'POST'])
def deletebrand(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    brand = Brand.query.get_or_404(id)
    if request.method == "POST":
        products = Addproduct.query.filter(Addproduct.category_id == id).all()
        for product in products:
            rates = Rate.query.filter(Rate.product_id == product.id).all()
            for rate in rates:
                db.session.delete(rate)
                db.session.commit()
            db.session.delete(product)
            db.session.commit()
        db.session.delete(brand)
        db.session.commit()
        flash(f"The brand {brand.name} was deleted from your database", "success")
        return redirect(url_for('brands'))
    flash(f"The brand {brand.name} can't be  deleted from your database", "warning")
    return redirect(url_for('brands'))


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getcat = request.form.get('category')
        cat = Category(name=getcat)
        db.session.add(cat)
        flash(f'The category {getcat} was added to your database', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('products/addbrand.html', title='Add category', user=user[0])


@app.route('/updatecat/<int:id>', methods=['GET', 'POST'])
def updatecat(id):
    if 'email' not in session:
        flash('Login first please', 'danger')
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method == "POST":
        updatecat.name = category
        flash(f'The category {updatecat.name} was updated', 'success')
        db.session.commit()
        return redirect(url_for('categories'))
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('products/updatebrand.html', title='Update cat', updatecat=updatecat, user=user[0])


@app.route('/deletecat/<int:id>', methods=['GET', 'POST'])
def deletecat(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    category = Category.query.get_or_404(id)
    if request.method == "POST":
        products = Addproduct.query.filter(Addproduct.category_id == id).all()
        for product in products:
            rates = Rate.query.filter(Rate.product_id == product.id).all()
            for rate in rates:
                db.session.delete(rate)
                db.session.commit()
            db.session.delete(product)
            db.session.commit()
        brands = Brand.query.filter(Brand.category_id == id).all()
        for brand in brands:
            db.session.delete(brand)
            db.session.commit()

        db.session.delete(category)
        db.session.commit()
        flash(f"The brand {category.name} was deleted from your database", "success")
        return redirect(url_for('categories'))
    flash(f"The brand {category.name} can't be  deleted from your database", "warning")
    return redirect(url_for('categories'))


@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))

    form = Addproducts(request.form)
    brands = Brand.query.all()
    categories = Category.query.all()
    if request.method == "POST":
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        desc = form.description.data
        brand = request.form.get('brand')
        category = request.form.get('category')

        image_1 = request.files.get('image_1')
        image_2 = request.files.get('image_2')
        image_3 = request.files.get('image_3')

        name_random_1 = secrets.token_hex(10) + "."
        name_random_2 = secrets.token_hex(10) + "."
        name_random_3 = secrets.token_hex(10) + "."

        # Save in firebase database
        save_link_1 = "" + name_random_1 + image_1.filename.split('.')[-1]
        save_link_2 = "" + name_random_2 + image_2.filename.split('.')[-1]
        save_link_3 = "" + name_random_3 + image_3.filename.split('.')[-1]

        # save static/images
        image_1 = photos.save(image_1, name=name_random_1)
        image_2 = photos.save(image_2, name=name_random_2)
        image_3 = photos.save(image_3, name=name_random_3)

        storage.child("images/" + save_link_1).put(os.path.join(current_app.root_path, "static/images/" + save_link_1))
        storage.child("images/" + save_link_2).put(os.path.join(current_app.root_path, "static/images/" + save_link_2))
        storage.child("images/" + save_link_3).put(os.path.join(current_app.root_path, "static/images/" + save_link_3))

        product = Addproduct(name=name, price=price, discount=discount, stock=stock, colors=colors, desc=desc,
                             category_id=category, brand_id=brand, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(product)
        flash(f'The product {product.name} was added in database', 'success')
        db.session.commit()
        return redirect(url_for('addproduct'))
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('products/addproduct.html', form=form, title='Add a Product', brands=brands,
                           categories=categories, user=user[0])


@app.route('/updateproduct/<int:id>', methods=['GET', 'POST'])
def updateproduct(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))

    # bucket.child('images').delete("30d516e59ed7deb97ed8.png")
    form = Addproducts(request.form)
    product = Addproduct.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')

    if request.method == "POST":
        product.name = form.name.data
        product.price = form.price.data
        product.discount = form.discount.data
        product.stock = form.stock.data
        product.colors = form.colors.data
        product.desc = form.description.data
        product.category_id = category
        product.brand_id = brand
        if request.files.get('image_1'):
            image_1 = request.files.get('image_1')
            name_random_1 = secrets.token_hex(10) + "."
            save_link_1 = "" + name_random_1 + image_1.filename.split('.')[-1]
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                storage.delete("images/" + product.image_1)
                product.image_1 = photos.save(image_1, name=name_random_1)
                storage.child("images/" + save_link_1).put(
                    os.path.join(current_app.root_path, "static/images/" + save_link_1))
            except:
                product.image_1 = photos.save(image_1, name=name_random_1)
                storage.child("images/" + save_link_1).put(
                    os.path.join(current_app.root_path, "static/images/" + save_link_1))
        if request.files.get('image_2'):
            image_2 = request.files.get('image_2')
            name_random_2 = secrets.token_hex(10) + "."
            save_link_2 = "" + name_random_2 + image_2.filename.split('.')[-1]
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
                storage.delete("images/" + product.image_2)
                product.image_2 = photos.save(image_2, name=name_random_2)
                storage.child("images/" + save_link_2).put(
                    os.path.join(current_app.root_path, "static/images/" + save_link_2))
            except:
                product.image_2 = photos.save(image_2, name=name_random_2)
                storage.child("images/" + save_link_2).put(
                    os.path.join(current_app.root_path, "static/images/" + save_link_2))
        if request.files.get('image_3'):
            image_3 = request.files.get('image_3')
            name_random_3 = secrets.token_hex(10) + "."
            save_link_3 = "" + name_random_3 + image_3.filename.split('.')[-1]
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
                storage.delete("images/" + product.image_3)
                product.image_3 = photos.save(image_3, name=name_random_3)
                storage.child("images/" + save_link_3).put(
                    os.path.join(current_app.root_path, "static/images/" + save_link_3))
            except:
                product.image_3 = photos.save(image_3, name=name_random_3)
                storage.child("images/" + save_link_3).put(
                    os.path.join(current_app.root_path, "static/images/" + save_link_3))
        db.session.commit()
        flash(f'The product was updated', 'success')
        return redirect(url_for('product'))

    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.colors.data = product.colors
    form.description.data = product.desc
    brand = product.brand.name
    category = product.category.name
    user = Admin.query.filter_by(email=session['email']).all()
    return render_template('products/updateproduct.html', form=form, title='Update Product', product=product,
                           brands=brands, categories=categories, user=user[0])


@app.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    product = Addproduct.query.get_or_404(id)
    if request.method == "POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
        except Exception as e:
            print(e)
        rates = Rate.query.filter(Rate.product_id == id).all()
        for rate in rates:
            db.session.delete(rate)
            db.session.commit()
        db.session.delete(product)
        db.session.commit()
        flash(f'The product {product.name} was delete from your record', 'success')
        return redirect(url_for('product'))
    flash(f'Can not delete the product', 'success')
    return redirect(url_for('product'))


@app.route('/addrate', methods=['GET', 'POST'])
def addrate():
    form = Rates(request.form)
    products_hot = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.price.desc()).limit(3).all()
    products_new = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).all()
    products_sell = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.discount.desc()).limit(10).all()
    products = {'hot': products_hot, 'new': products_new, 'sell': products_sell, 'average': medium()}
    product_id = -1
    if request.method == "POST":
        register_id = request.form.get('register_id')
        product_id = request.form.get('product_id')
        desc = request.form.get('desc')
        rate_number = request.form.get('select')
        rate = Rate(register_id=register_id, product_id=product_id, desc=desc, rate_number=rate_number)
        db.session.add(rate)
        flash(f'The rate {register_id} was added to your database', 'success')
        db.session.commit()
        return redirect(url_for('detail', id=product_id))
        # return "OK this is a post method"
    rates = Rate.query.filter(Rate.product_id == product_id).order_by(Rate.id.desc()).all()
    product = Addproduct.query.get_or_404(product_id)
    return render_template('products/product.html', title='Add rate', form=form, products=products, rates=rates,
                           product=product, brands=brands(), registers=registers(), categories=categories())


@app.route('/detail/id_<int:id>')
def detail(id):
    kt = False
    customer = None
    if current_user.is_authenticated:
        customer = Register.query.get_or_404(current_user.id)
        rates = Rate.query.order_by(Rate.id.desc()).all()
        for rate in rates:
            if id == rate.product_id and customer.id == rate.register_id:
                kt = True
    form = Rates(request.form)
    rates = Rate.query.filter(Rate.product_id == id).order_by(Rate.id.desc()).all()
    products_hot = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.price.desc()).limit(3).all()
    products_new = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).limit(2).all()
    products_sell = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.discount.desc()).limit(10).all()
    products = {'hot': products_hot, 'new': products_new, 'sell': products_sell, 'average': medium()}
    product = Addproduct.query.get_or_404(id)
    # products = Addproduct.query.filter_by(id='id')
    return render_template('products/product.html', product=product, products=products, brands=brands(), form=form,
                           rates=rates, registers=registers(), categories=categories(), customer=customer, kt=kt)


@app.route('/category/discount/<int:start>-<int:end>')
def get_discount(start, end):
    page = request.args.get('page', 1, type=int)
    product_discount = Addproduct.query.filter(Addproduct.discount >= start, Addproduct.discount < end) \
        .order_by(Addproduct.id.desc()).paginate(page=page, per_page=9)
    products_new = Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).limit(2).all()
    products = {'all': product_discount, 'new': products_new, 'average': medium()}
    return render_template('products/category.html', products=products, brands=brands(), categories=categories())


@app.route('/search', methods=['GET', 'POST'])
def search():
    value = request.form['search']
    search = "%{}%".format(value.lower())
    page = request.args.get('page', 1, type=int)
    product = Addproduct.query.filter(Addproduct.name.ilike(search)).paginate(page=page, per_page=9)
    products = {'all': product, 'average': medium()}
    return render_template('products/category.html', get_search=value, products=products, brands=brands(),
                           categories=categories())
