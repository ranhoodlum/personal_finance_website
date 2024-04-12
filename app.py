from flask import Flask, render_template, request, session

# initializing the app
app = Flask(__name__)

@app.route("/index.html")
@app.route("/")
def index():
    return render_template('index.html', title="Home")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method:
        return render_template("login.html")
    else:
        