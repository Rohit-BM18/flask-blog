from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


 

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created successfully for {form.username.data}! ", "success")
        return redirect(url_for('func'))
    return render_template("register.html", title = "Register", form = form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=="admin@flaskmail.com" and form.password.data=="password" :
            flash("user successfully logged in!","success")
            return redirect(url_for('func'))
        else:
            flash("Unsuccessful attempt, Invalid Username or Password","danger")
        
    return render_template('login.html', title = "login", form = form)
