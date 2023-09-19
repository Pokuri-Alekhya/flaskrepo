from project import app,render_template
from project.modules import User
from project.forms import RegisterForm,LoginForm,searchForm
from project import db 
from flask import redirect,url_for,flash,request,jsonify
from flask_login import login_user,logout_user,login_required,current_user
@app.route('/display')
def display():
    user=User.query.all()

    return render_template("display.html",items=user)
@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/details')
@login_required
def details():
    return render_template("details.html")
@app.route('/master')
@login_required
def master():
    if current_user.Role=="admin":
        user=User.query.all()
        form=searchForm()
        return render_template("master.html",items=user,form=form)
    else:
        flash('employee can not access to master screen',category="danger")
        return redirect(url_for('home'))
    
@app.route('/register',methods=['POST','GET'])
def register():
    form=RegisterForm()
    if current_user.is_authenticated:
        role='employee'
    else:
        role='admin'
    
    if form.validate_on_submit():
        create_acc=User(Firstname=form.Firstname.data,
        Lastname=form.Lastname.data,
        Email=form.Email.data,
        PhoneNumber=form.PhoneNumber.data,
        DOB=form.DOB.data,
        Address=form.Address.data,
        password=form.Password.data,
        Role=role)
        db.session.add(create_acc)
        db.session.commit()
        flash(f' Registration Successful',category="success")
        return redirect(url_for('home'))
    if form.errors!={}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating user:{err_msg}',category="danger")
    return render_template("register.html",form=form)


@app.route('/login',methods=['POST','GET'])
def login():
    lf=LoginForm()
    if lf.validate_on_submit():
        attempted_user=User.query.filter_by(Email=lf.Username.data,Role=lf.Logintype.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=lf.Password.data ):
            login_user(attempted_user)
            flash(f'Your are logged in Successfully...!!',category="success")
            return redirect(url_for('details'))
            
        else:
            flash(f'Username or password or role is not correct ,please try again with correct credentials',category="danger")

    return render_template("login.html",lf=lf)
@app.route('/admin')
@login_required
def admin():

    return render_template("admin.html")
@app.route('/logout')
def logout():
    logout_user()
    flash(f'you are logged out',category='info')
    return redirect(url_for('home'))

@app.route('/api/search')
@login_required
def search_employees_api():
    name = request.args.get('name')
    address = request.args.get('address')
    
    if name and address:
        employees = User.query.filter(User.Firstname.ilike('%{}%'.format(name))|User.Lastname.ilike('%{}%'.format(name)), User.Address.ilike('%{}%'.format(address))).all()
        
        employee_data = []
        for employee in employees:
            employee_data.append({
                
                'Firstname': employee.Firstname,
                'Lastname': employee.Lastname,
                'Email': employee.Email
            
            })
        
        
           

        return jsonify({'employees': employee_data})
        
            
    else:
        return jsonify({'error': 'Invalid search parameters'}) 