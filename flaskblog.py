from flask import Flask
app = Flask(__name__)

@app.route("/")
def func():
    return "Hello world"

@app.route("/about")
def about_page():
    return "About page"

@app.route("/contact")
def contact_page():
    return "contact page"

if(__name__ == "__main__"):
    
    app.run()