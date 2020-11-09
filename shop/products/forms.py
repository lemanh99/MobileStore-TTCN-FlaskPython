from wtforms import Form, SubmitField, IntegerField, FloatField, StringField, TextAreaField, validators, DecimalField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    colors = StringField('Colors', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])

    image_1 = FileField('Image 1',
                        validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'], 'Images only please'), FileRequired()])
    image_2 = FileField('Image 2',
                        validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'], 'Images only please'), FileRequired()])
    image_3 = FileField('Image 3',
                        validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'], 'Images only please'), FileRequired()])


class Rates(Form):
    register_id = IntegerField('Register_id', [validators.DataRequired()])
    product_id = IntegerField('Product_id', [validators.DataRequired()])
    desc = TextAreaField('Desc', [validators.DataRequired()])
