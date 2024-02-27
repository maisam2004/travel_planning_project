import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager  

import psycopg2
import smtplib
if os.path.exists("env.py"):
    import env
from flask_mail import Mail

app = Flask(__name__)






login_manager = LoginManager(app)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


mail = Mail(app)
app.config['MAIL_SERVER'] = os.environ.get("MAIL_SERVER")
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")



db = SQLAlchemy(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)

from travel_planning import routes
login_manager.login_view = 'login'



def split_by_dash(text):
    return text.split('//')[0].strip()  # Return the first part after splitting by '//'

def split_by_dash_second(text):
    try:
        return text.split('//')[1].strip()  # Return the second part after splitting by '//'
    except IndexError:
        return ''  # Return an empty string if '//' is not found or if there's an IndexError
 # Return the second part after splitting by '//'
    
# Register the custom filter with Jinja2
app.jinja_env.filters['split_by_dash'] = split_by_dash
app.jinja_env.filters['split_by_dash_second'] = split_by_dash_second
