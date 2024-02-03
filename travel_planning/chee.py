from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from travel_planning import app, db, login_manager
from .models import User, Destination
from .forms import SignupForm, ResetPasswordForm, ResetPasswordRequestForm, AddDestinationForm
from flask_mail import Message
from . import mail
import os
import secrets
from werkzeug.utils import secure_filename

@app.route('/explore', methods=['GET', 'POST'])
@login_required
def explore():
    form = AddDestinationForm()

    if form.validate_on_submit():
        new_destination_name = form.newDestinationName.data
        new_destination_location = form.newDestinationLocation.data
        new_destination_image = form.newDestinationImage.data

        # Save the uploaded image and get the file path
        image_path = save_destination_image(new_destination_image)

        # Create a new Destination object and add it to the database
        new_destination = Destination(
            name=new_destination_name,
            location=new_destination_location,
            image=image_path,
            user_id=current_user.id  # Associate the destination with the current user
        )

        db.session.add(new_destination)
        db.session.commit()

        flash('Destination added successfully!', 'success')
        return redirect(url_for('explore'))

    # Retrieve destinations for the current user
    user_destinations = Destination.query.filter_by(user_id=current_user.id).all()

    return render_template('explore.html', form=form, user_destinations=user_destinations)


def save_destination_image(image):
    # Handle the image upload, save it to a folder or cloud storage
    # For now, save it to the 'static/images/destinations' folder
    destination_images_folder = os.path.join(app.root_path, 'static', 'images', 'destinations')
    
    # Ensure the folder exists
    os.makedirs(destination_images_folder, exist_ok=True)

    # Generate a unique filename
    filename = secrets.token_hex(8) + secure_filename(image.filename)

    # Save the file to the destination folder
    image_path = os.path.join(destination_images_folder, filename)
    image.save(image_path)

    return image_path
