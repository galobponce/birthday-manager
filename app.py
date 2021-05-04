from flask import Flask, render_template, redirect, request, session, flash, jsonify
from flask_session import Session

from cs50 import SQL

from helpers import validate_date, login_required

from datetime import date

from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Configure sql library
db = SQL("sqlite:///birthdays.db")

# Configure session library 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET"])
@login_required
def index():
  """ Renders menu """
  # Takes user birthdays and returns them to index.hmtl
  rows = db.execute("SELECT * FROM birthdays WHERE user_id IS (?) ORDER BY month ASC;", session["user_id"])
  return render_template('menu.html', rows = rows)


@app.route("/home", methods=["GET"])
def home():
  """ Renders home """
  return render_template("home.html")


@app.route("/login", methods=["POST"])
def login():
  """ Lets user Log In """
  session.clear() # Clears session data

  # Checks emptiness
  if not request.form.get("username"):
    flash("Must provide username")
    return redirect("/home")

  if not request.form.get("password"):
    flash("Must provide password")
    return redirect("/home")

  # Gets username's given password
  row_list = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

  # Checks if username and passowrd does match
  if len(row_list) != 1 or not check_password_hash(row_list[0]["hash"], request.form.get("password")):
    flash("Username and Password given does not match")
    return redirect("/home")

  session["user_id"] = row_list[0]["id"] # Stores user_id in session

  flash("Successfully logged in")
  return redirect("/")


@app.route("/logout", methods=["GET"])
@login_required
def logout():
  """ Clears session data """
  session.clear()
  flash("Successfully logged out")
  return redirect("/home")


@app.route("/register", methods=["POST"])
def register():
  """ Register a user in database """
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
  row_list = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

  if row_list:
    flash("Username already exists")
    return redirect("/home")

  # Inserts new user into database
  db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get('username'), generate_password_hash(request.form.get('password')))

  flash("You were successfully registered!")
  return redirect("/home")


@app.route("/add", methods=["POST"])
@login_required
def add():
  """ Adds a birthday to database """
  name = request.form.get("name")
  month = request.form.get("month")
  day = request.form.get("day")
  year = date.today().year
  
  # Validates data given
  if not name or not month or not day:
    flash("Must provide birthday's data")
    return redirect("/")

  if not validate_date(int(year), int(month), int(day)):
    flash("Must provide a valid date")
    return redirect("/")

  # Adds birthday to database using user's id
  db.execute("INSERT INTO birthdays (user_id, name, month, day) VALUES (?, ?, ?, ?)", session["user_id"], name, month, day)

  flash("Birthday successfully added")
  return redirect("/")


@app.route("/delete", methods=["POST"])
@login_required
def delete():
  """ Deletes a birthday from database """
  idToRemove = request.form.get("id")
  db.execute("DELETE FROM birthdays WHERE birthday_id IS ? AND user_id IS ?", idToRemove, session["user_id"])
  flash("Birthday succeessfully removed")
  return redirect("/")


@app.route("/search", methods=["GET"])
@login_required
def search():
    """ Searches throught all names by filter """
    q = request.args.get("q")
    if q:
        rows = db.execute("SELECT * FROM birthdays WHERE name LIKE ? AND user_id IS (?)", "%" + q + "%", session["user_id"])
    else:
        rows = []
    # JSONs database's rows
    return jsonify(rows)