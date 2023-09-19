from flask import Flask,render_template,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'   
db=SQLAlchemy(app) 
bcrypt=Bcrypt(app) 

app.config['SECRET_KEY']='03e0e468a8bbbcace0c6d56d'

login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category="info"#to apply category to flash message
from project import routes