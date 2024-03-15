import os 
from flask import Flask,Markup
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager  
import re

import psycopg2
import smtplib
if os.path.exists("env.py"):
    import env
from flask_mail import Mail,Message
import sqlalchemy.dialects.postgresql




app = Flask(__name__)
debug= os.environ.get('DEBUG')




login_manager = LoginManager(app)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
uri = os.environ.get("DATABASE_URL")  # or other relevant config var

if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = uri

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



app.config['MAIL_SERVER'] = os.environ.get("MAIL_SERVER")
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'maisam2004@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
mail = Mail(app)


db = SQLAlchemy(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)

from travel_planning import routes
login_manager.login_view = 'login'


#these filter used to remove part displayed text for travel packages card in card and modal
def split_by_dash(text):
    """Splits a string by the first occurrence of '//' and returns the first part, stripped of whitespace.

  Args:
      text (str): The string to split.

  Returns:
      str: The first part of the string before the first '//', stripped of leading and trailing whitespace.
          If '//' is not found, the original string is returned stripped.
  """
    return text.split('//')[0].strip()  # Return the first part after splitting by '//'

def split_by_dash_second(text):
    """Splits a string by the first occurrence of '//' and returns the second part, stripped of whitespace.

  Handles potential IndexError if '//' is not found or if there are less than two parts after splitting.

  Args:
      text (str): The string to split.

  Returns:
      str: The second part of the string after the first '//', stripped of leading and trailing whitespace.
          If '//' is not found, an empty string is returned.
  """

    try:
        return text.split('//')[1].strip()  # Return the second part after splitting by '//'
    except IndexError:
        return ''  # Return an empty string if '//' is not found or if there's an IndexError
 # Return the second part after splitting by '//'
    
# Register the custom filter with Jinja2
app.jinja_env.filters['split_by_dash'] = split_by_dash
app.jinja_env.filters['split_by_dash_second'] = split_by_dash_second


#filter for label in reset form label tag generated by flask
def strip_label_tags(text):
    """
    Remove <label> and </label> tags from the given text.

    Args:
        text (str): The input text that may contain <label> tags.

    Returns:
        str: The input text with <label> and </label> tags removed.
    """
    return Markup(re.sub(r'</?label.*?>', '', str(text)))

# Register the custom filter
app.jinja_env.filters['strip_label_tags'] = strip_label_tags


def replace_backslashes(url):
    """Replaces backslashes with forward slashes and trims for static URLs."""
    url =  re.sub(r'%5C', '/', url)
    url = url[url.find('static'):]
    return url
app.jinja_env.filters['replace_backslashes'] = replace_backslashes


def remove_csrf_id(html):
    """Remove the id attribute from the CSRF token field."""
    #return Markup(html.replace('id=', 'list='))
    return Markup(html.replace('id=', 'aria-label='))
    

app.jinja_env.filters['remove_csrf_id'] = remove_csrf_id

