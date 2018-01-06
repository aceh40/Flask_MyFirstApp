
"""
Spyder Editor

This is a temporary script file.
"""

from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import TextField, PasswordField, BooleanField, SubmitField
from wtforms import validators

msgNotEmail = 'This is not a valid email address.'
msgPassMatch = "Passwords do not match"

class RegistrationForm(Form):
	firstName = TextField('First Name:', [validators.Length(min=1, max=50)])
	lastName = TextField('Last Name:', [validators.Length(min=1, max=50)])
	email = TextField('Email Address:', [validators.Length(min=4, max=50)
											, validators.Email(message=msgNotEmail)])
	password = PasswordField('Password:', [validators.Length(min=4, max=20)])
	re_password = PasswordField('Confirm Password:'
								, [validators.Length(min=4, max=20)
									,validators.EqualTo('password', message=msgPassMatch )])
	acceptTerms = BooleanField('I accept the <a href="/tos/">Terms of Service</a> etc...', [validators.Required()])
	submit = SubmitField('Sign In')
	




