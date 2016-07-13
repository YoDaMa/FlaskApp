from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
# Not using forms yet so it's okay to not worry about this...
class LoginForm(Form):
	openid = StringField('oepnid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)