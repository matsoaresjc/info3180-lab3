from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class User_form(FlaskForm):
	name = StringField('Please enter your full name',validators = [DataRequired()])
	email = StringField('Please enter your email',validators = [DataRequired()])
	subject = StringField('Please enter the subject of your message',validators = [DataRequired()])
	msg = StringField('Please enter your message',validators = [DataRequired()])

