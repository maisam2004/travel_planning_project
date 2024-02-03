from travel_planning import db
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from datetime import datetime
bcrypt = Bcrypt()  # Using bcrypt for password hashing

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    image = db.Column(db.String(255))  # Store the file path or URL of the image
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

"""
class Category(db.Model):
    #schema for category model
    id = db.Column(db.Integer,primary_key = True)
    category_name = db.Column(db.String(25),unique=True,nullable = False) #make sure is uinque
    tasks = db.relationship("Task",backref ="category",cascade = "all, delete",lazy = True)

    def __repr__(self):
        #repersent itesef with string
        return self.category_name


class Task(db.Model):
    #schema for task model
    id = db.Column(db.Integer,primary_key = True)
    task_name = db.Column(db.String(50),unique = True,nullable = False)
    task_description = db.Column(db.Text,nullable = False)
    is_urgent = db.Column(db.Boolean,default = False,nullable = False)
    due_date = db.Column(db.Date,nullable = False)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id',ondelete = "CASCADE"),nullable = False )
    #other types >> db.Integer,db.Float 
    def __repr__(self):
        return "# {0} - Task: {1} | Urgent: {2}".format(self.id,self.task_name,self.is_urgent) """