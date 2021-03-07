from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fbc0fa1f087697dfe11483079b0fa1b9'

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