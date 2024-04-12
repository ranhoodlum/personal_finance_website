from flask import Flask, render_template, request, session

# initializing the app
app = Flask(__name__)

@app.route("/index.html")
@app.route("/")
def index():
    return render_template('index.html', title="Home")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
    return render_template("login.html")
        