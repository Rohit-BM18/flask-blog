from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, bcrypt, db
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required



blog_posts = [
    {
     'author':'Rohit',
     'title': 'GANs',
     'content': 'intro to GANs',
     'date_posted': '1st March 2021'
    },

    {
     'author':'Toby',
     'title': 'CNNs',
     'content': 'intro to CNNs',
     'date_posted': '2nd March 2021'
    }
]

"""
REMINDER to define endpoints for additional features


>> chat flask-socket.io
>> video calls webrtc
>> make a anon addressal portal
>> also an endpoint for hosting podcasts

"""

@app.route("/")
@app.route("/home") 
def func():
    return render_template("home.html", posts=blog_posts ,title="Blog-Homepage")

@app.route("/about")
def about_page():
    return render_template("about.html", title = "About-Us")
    
@app.route("/contact")
def contact_page():
    return render_template("contact.html", title = "Contact")

@app.route('/register', methods=['GET','POST'])
def registration():

    if current_user.is_authenticated:
        flash(f'logged in as {current_user.username}')
        return redirect(url_for('func'))
        

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created!. You can now log in", "success")
        return redirect(url_for('login'))
    return render_template("register.html", title = "Register", form = form)


@app.route('/login', methods=['GET','POST'])
def login():

    if current_user.is_authenticated:
        flash(f'logged in as {current_user.username}')
        return redirect(url_for('func'))

    form = LoginForm()
    if form.validate_on_submit():
            user  = User.query.filter_by(email = form.email.data).first()
            
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')

                if next_page:
                    return redirect(next_page)
                else:
                    return redirect(url_for('func'))
            else:
                flash("Unsuccessful attempt, Invalid email or Password","danger")
        
    return render_template('login.html', title = "login", form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('func'))


@app.route('/account')
@login_required
def account():
    
    return render_template('account.html', title='Account')