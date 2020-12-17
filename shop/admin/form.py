from wtforms import BooleanField, StringField, PasswordField, validators, ValidationError, RadioField, SubmitField
from flask_wtf import FlaskForm, Form
from shop.customers.models import Register
import phonenumbers


class RegistrationForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


    

class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [validators.DataRequired()])




class CustomerRegisterForm(FlaskForm):
    username = StringField('Username: ', [validators.DataRequired(), validators.Length(min=4, max=20)])
    first_name = StringField('Fist Name: ')
    last_name = StringField('Last Name: ')
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    phone_number = StringField('Phone: ', [validators.DataRequired()])
    gender = RadioField('Gender:', default='M', choices=[('M', 'Male'), ('F', 'Female')])
    password = PasswordField('Password: ', [validators.DataRequired(),
                                            validators.EqualTo('confirm', message=' Both password must match! ')])
    confirm = PasswordField('Repeat Password: ', [validators.DataRequired()])

    submit = SubmitField('Register')

    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError("This username is already in use!")

    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError("This email address is already in use!")

    def validate_phone_number(self, phone_number):
        if Register.query.filter_by(phone_number=phone_number.data).first():
            raise ValidationError("This phonenumber is already in use!")

        try:
            input_number = phonenumbers.parse(phone_number.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+84" + phone_number.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
