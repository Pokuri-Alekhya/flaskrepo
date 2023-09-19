from project import db,login_manager
from project import bcrypt
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    Firstname=db.Column(db.String(length=30))
    Lastname=db.Column(db.String(length=30),nullable=True)
    Email=db.Column(db.String(length=100),nullable=False)
    PhoneNumber=db.Column(db.Integer)
    DOB=db.Column(db.Date())
    Address=db.Column(db.String(length=200))
    Password=db.Column(db.String(length=20)) 
    Role=db.Column(db.String(length=10),nullable=False)
    @property
    def password(self):
        return self.password
    @password.setter
    def password(self,text):
        self.Password=bcrypt.generate_password_hash(text).decode('utf-8')
    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.Password,attempted_password)
             