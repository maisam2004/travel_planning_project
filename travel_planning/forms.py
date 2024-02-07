# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField,FileField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])



class ResetPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Reset Password')
    
class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class AddDestinationForm(FlaskForm):
    name = StringField('Destination Name', validators=[DataRequired()])
    location = StringField('Destination Location', validators=[DataRequired()])
    image = FileField('Upload Image')
    submit = SubmitField('Add Destination')


class EditDestinationForm(FlaskForm):
    name = StringField('Destination Name', validators=[DataRequired()])
    location = StringField('Destination Location', validators=[DataRequired()])
    
    image = FileField('Update Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Images only!')])
    submit = SubmitField('Save Changes')

    def populate_obj(self, obj):
        # Update the form fields with existing data
        obj.name.data = self.name.data
        obj.location.data = self.location.data
        # Update other fields as needed

class AddTravelPackageForm(FlaskForm):
    name = StringField('Travel Package Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    hotel = StringField('Hotel')
    latitude = StringField('Latitude', validators=[DataRequired()])  # Add latitude field
    longitude = StringField('Longitude', validators=[DataRequired()])  # Add longitude field
    image1 = FileField('Image 1')  # Add this line for the first image
    image2 = FileField('Image 2')  # Add this line for the second image
    image3 = FileField('Image 3')  # Add this line for the third image
    submit = SubmitField('Add Travel Package')

class AddTravelPackageImageForm(FlaskForm):
    filename = FileField('Image', validators=[DataRequired()])
    submit = SubmitField('Add Image')