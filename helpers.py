from flask import redirect, render_template, request, session

from datetime import datetime

from functools import wraps

def validate_date(year, month, day):
  """ Given a year, month and a day, returns True / False depending if date is valid """
  try:
    newDate = datetime(year, month, day)
    return True
  except ValueError:
    return False

# Decorator function to require a user being logged in
def login_required(f):
  """ https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/ """
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if not session.get("user_id"):
      return redirect("/home")
    return f(*args, **kwargs)
  return decorated_function