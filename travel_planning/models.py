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
    destinations = db.relationship('Destination', backref='user', lazy=True)
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class UserImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_path = db.Column(db.String(255), nullable=False)
    def __repr__(self):
        return f"UserImage(user_id={self.user_id}, image_path='{self.image_path}')"

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)  # New field for description
    likes = db.Column(db.Integer, default=0)  # New field for likes
    image = db.Column(db.String(255))  # Store the file path or URL of the image
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class TravelPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    location = db.Column(db.String(150) )
    hotel = db.Column(db.String(100))
    hotel_description = db.Column(db.Text)
    duration= db.Column(db.String(100))
    package_price = db.Column(db.Float) 
    latitude = db.Column(db.String(50), nullable=False)  # Add latitude column
    longitude = db.Column(db.String(50), nullable=False)  # Add longitude column
    images = db.relationship('TravelPackageImage', backref='travel_package', lazy=True)
 


class TravelPackageImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    travel_package_id = db.Column(db.Integer, db.ForeignKey('travel_package.id'), nullable=False)



#desire holidy
class WishedHoliday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    holiday_type = db.Column(db.String(50), nullable=False)
    travel_duration = db.Column(db.Integer, nullable=False)
    price_range = db.Column(db.String(100), nullable=False)
    travel_time = db.Column(db.String(100), nullable=False)
    departure_location = db.Column(db.String(100), nullable=False)
    additional_info = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # ForeignKey relationship

    # relationship with the User model
    user = db.relationship('User', backref=db.backref('wished_holidays', lazy=True))





#call back requests

class UsersCallbackRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    package_name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text)

    def __repr__(self):
        return f'<UsersCallbackRequest {self.id}>'
