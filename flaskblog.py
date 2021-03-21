from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fbc0fa1f087697dfe11483079b0fa1b9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


 

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



if(__name__ == "__main__"):
    
    app.run()