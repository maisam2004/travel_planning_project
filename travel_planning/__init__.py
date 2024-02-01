import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager  
import psycopg2
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

login_manager = LoginManager(app)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")





app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)

from travel_planning import routes
login_manager.login_view = 'login'