from travel_planning import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)






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