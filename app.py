from flask import Flask, render_template, redirect, request, session, flash, jsonify
from flask_session import Session

# from cs50 import SQL

from helpers import validate_date, login_required

from datetime import date

from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Configure sql library
# db = SQL("sqlite:///birthdays.db")

# Configure session library 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET"])
@login_required
def index():
  # Takes user birthdays and returns them to index.hmtl
  rows = None # db.execute("SELECT * FROM birthdays WHERE user_id IS (?) ORDER BY month ASC;", session["user_id"])
  return render_template('main.html', rows = rows)


@app.route("/home", method=["GET"])
def home():
  return render_template("home.html")


@app.route("/login", methods=["POST"])
def login():
  session.clear() # Clears session data

  # Checks emptiness
  if not request.form.get("username"):
    flash("Must provide username")
    return redirect("/home")

  if not request.form.get("password"):
    flash("Must provide password")
    return redirect("/home")

  # Gets username's given password
  row_list = None # db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

  # Checks if username and passowrd does match
  if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
    flash("Username and Password given does not match")
    return redirect("/home")

  session["user_id"] = rows[0]["id"] # Stores user_id in session

  flash("Successfully logged in")
  return redirect("/home")


@app.route("/logout", methods=["GET"])
@login_required
def logout():
  session.clear()
  flash("Successfully logged out")
  return redirect("/home")


@app.route("/register", methods=["POST"])
def register():
  session.clear() # Clears session data

  if not request.form.get("username"):
    flash("Must provide username")
    return redirect("/home")
  
  if not request.form.get("password"):
    flash("Must provide password")
    return redirect("/home")

  if request.form.get("password") != request.form.get("confirmation"):
    flash("Passwords does not match")
    return redirect("/home")

  # Checks if username already exists
  row_list = None # db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

  if row_list:
    flash("Username already exists")
    return redirect("/home")

  # Inserts new user into database
  # db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get('username'), generate_password_hash(request.form.get('password')))

  flash("You were successfully registered!")
  return redirect("/home")