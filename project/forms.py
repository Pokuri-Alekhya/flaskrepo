from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,DateField,EmailField,SelectField,TelField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from project.modules import User
class RegisterForm(FlaskForm):
    def validate_Email(self,email_to_check):
        user=User.query.filter_by(Email=email_to_check.data).first()
        if user:
            raise ValidationError('Email already exists!!please try with different mail')
   
    #Role=SelectField(label="Role",choices=[('','Select Role'),('admin','Admin'),('employee','Employee')])
    Firstname=StringField(label="Firstname",validators=[Length(min=2,max=30),DataRequired()])
    Lastname=StringField(label="Secondname",validators=[DataRequired()])
    Email=EmailField(label="Email id",validators=[Email(),DataRequired()])
    PhoneNumber=TelField(label="Phone Number",validators=[Length(min=10,max=10)])
    DOB=DateField(label="Date of Birth")
    
    Address=TextAreaField(label="Address",validators=[DataRequired()])
    Password=PasswordField(label="Password",validators=[DataRequired()])
    
    Confirmpwd=PasswordField(label='confirm Password', validators=[DataRequired(),
                         EqualTo('Password',
                         message="Passwords must match")])
    submit=SubmitField(label="submit")


class LoginForm(FlaskForm):
   #def validate_Username(self,email_to_check):
        #user=User.query.filter_by(Email=email_to_check.data).first()
        #if user:
            #return
        #else:
            #raise ValidationError('User do not  exists!!please enter correct username')
    
    Username=EmailField(label="Email id")
    Logintype=SelectField(label="Login Type",choices=[('','Select LoginType'),('admin','Admin'),('employee','Employee')])
    Password=PasswordField(label="Password")
    submit=SubmitField(label="submit")


class searchForm(FlaskForm):
    Name=StringField(label='Name',validators=[DataRequired()])
    Address=StringField(label='Address',validators=[DataRequired()])
    search=SubmitField(label='Search')
    

    

