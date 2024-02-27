from flask import render_template,redirect,request,url_for,flash,current_app,jsonify
from flask_login import login_user, logout_user, login_required,current_user
from travel_planning import app,db,login_manager
from .models import User,Destination,TravelPackage,TravelPackageImage,WishedHoliday,UserImage
from .forms import SignupForm , ResetPasswordForm,ResetPasswordRequestForm,AddDestinationForm,EditDestinationForm,AddTravelPackageForm,WishedHolidayForm,UserImageForm
from flask_mail import Message
from . import mail
import os
import secrets 
from werkzeug.utils import secure_filename
import logging
import sqlalchemy.dialects.postgresql

#from travel_planning.models import Category , Task



# route for contact_us page
@app.route('/contact_us')
def contact_us():
    
    return render_template('contact_us.html'  )


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    

    # Retrieve wished holidays associated with the current user
    wishes = WishedHoliday.query.filter_by(user_id=current_user.id).all()

    # Retrieve user's image if it exists
    user_image = UserImage.query.filter_by(user_id=current_user.id).first()
    current_user_image = user_image.image_path if user_image else None
    just_path = current_user_image.split('static\\') 
    current_user_image1 = just_path[1].replace("\\", "/")
    
    
    
    # Create form instance
    user_image_form = UserImageForm()

    if user_image_form.validate_on_submit():
        # Save the uploaded image
        image_file = user_image_form.image.data
        filename = secure_filename(image_file.filename)
        
        # Define the file path in the static/images folder
        filepath = os.path.join(current_app.root_path, 'static', 'images', filename)
        image_file.save(filepath)

        # Check if user already has an image record
        if user_image:
            user_image.image_path = filepath
        else:
            # Create a new image record for the user
            user_image = UserImage(user_id=current_user.id, image_path=filepath)
            db.session.add(user_image)

        db.session.commit()
        flash('Profile image uploaded successfully!', 'success')
        return redirect(url_for('account'))

    # Pass form and current user's image path to the template
    return render_template('account.html', user=current_user, current_user_image1=current_user_image1, user_image_form=user_image_form,wishes=wishes )



@app.route('/about', methods=['POST','GET'])
def about():
    
    return render_template('about_us.html' )

@app.route('/', methods=['POST','GET'])
def home():
    
    travel_packages = TravelPackage.query.all()
    # Initialize the holiday wish
    form = WishedHolidayForm()
    if form.validate_on_submit():
        wished_holiday = WishedHoliday(
            holiday_type=form.holiday_type.data,
            travel_duration=form.travel_duration.data,
            price_range=str(form.price_range.data),
            travel_time=str(form.travel_time.data),
            departure_location=str(form.departure_location.data),
            additional_info=form.additional_info.data,
            user_id=current_user.id  # Ensure current_user is correct
        )
        db.session.add(wished_holiday)
        try:
            db.session.commit()  # Commit after adding to the session
            flash('Your wished holiday has been submitted successfully!', 'success')
            return redirect(url_for('wished_holiday'))
        except Exception as e:
            logging.error(f"Error saving wished holiday: {e}")
            print('An error occurred while submitting your wish.', 'danger')
            return render_template('home.html', form=form )  # Handle exception
    
    return render_template('home.html', travel_packages=travel_packages,form=form )

## dealing with like button 







@app.route('/wished_holiday')
@login_required
def wished_holiday():
    wishes = WishedHoliday.query.filter_by(user_id=current_user.id).all()
    last_wish = WishedHoliday.query.filter_by(user_id=current_user.id).order_by(WishedHoliday.id.desc()).first()

    return render_template('wished_holiday.html', wishes=last_wish) 

#delete wished holiday ===========================================
@app.route('/account/delete/<int:wishedholiday_id>', methods=['POST'])
@login_required
def delete_wished(wishedholiday_id):
    # Check if the user is authenticated

    wished = WishedHoliday.query.get_or_404(wishedholiday_id)


    # Delete the destination from the database
    db.session.delete(wished)
    db.session.commit()

    flash('Destination deleted successfully!', 'success')
    return redirect(url_for('account'))
#====================================================================
@app.route('/explore', methods=['GET', 'POST'])
def explore():
    
    form = AddDestinationForm()
    # Check if the user is authenticated
    if current_user.is_authenticated:
        # User is logged in, allow additional actions
        

        if form.validate_on_submit():
            # Process and save the form data...

            # Save the uploaded image and get the file path
            image_path = save_destination_image(form.image.data)

            # Create a new Destination object and add it to the database
            new_destination = Destination(
                name=form.name.data,
                location=form.location.data,
                description=form.description.data,
                image=image_path,
                user_id=current_user.id
            )

            db.session.add(new_destination)
            db.session.commit()

            flash('Destination added successfully!', 'success')
            print("Destination added successfully!")
            return redirect(url_for('explore'))

        # Retrieve destinations for the all users
        #user_destinations = Destination.query.filter_by(user_id=current_user.id).all()
        all_destinations = Destination.query.order_by(Destination.name).all()
        #return render_template('explore.html', form=form, user_destinations=user_destinations)

    else:
        # User is not logged in, only allow viewing
        
        all_destinations = Destination.query.all()
    return render_template('explore.html', form=form,all_destinations=all_destinations )



#liked destinations 
from flask import request, jsonify

@app.route('/like', methods=['POST'])
def like_destination():
    destination_id = request.form['destination_id']  #  the destination ID
    destination = Destination.query.get(destination_id)
    if destination:
        # Increment the likes count
        destination.likes += 1
        db.session.commit()
        return jsonify({'success': True, 'likes': destination.likes})
    else:
        return jsonify({'success': False, 'error': 'Destination not found'})



## edit  destination -----------------

@app.route('/explore/edit/<int:destination_id>', methods=['GET', 'POST'])
def edit_destination(destination_id):
    
    # Check if the user is authenticated
    if not current_user.is_authenticated:
        flash('You need to log in to edit destinations.', 'danger')
        return redirect(url_for('login'))

    # Retrieve the destination to edit
    destination = Destination.query.get_or_404(destination_id)

    # Check if the current user is the owner of the destination
    if current_user.id != destination.user_id:
        flash('You do not have permission to edit this destination.', 'danger')
        return redirect(url_for('explore'))

    # Use the EditDestinationForm to handle the edit form
    form = EditDestinationForm(obj=destination)

    if form.validate_on_submit():
        # Process and save the form data
        destination.name = form.name.data
        destination.location = form.location.data
        destination.description = form.description.data
        if form.image.data:
            if isinstance(form.image.data, str):
            # If form.image.data is a string, it means no new image was provided,
            # so we keep the existing image
                destination.image = form.image.data
            else:
            # Process and save the uploaded image
                destination.image = save_destination_image(form.image.data)

        # Save the changes to the database
        db.session.commit()

        flash('Destination edited successfully!', 'success')
        return redirect(url_for('explore'))

    return render_template('edit_destination.html', form=form, destination=destination )

    
## delete destination -----------------
@app.route('/explore/delete/<int:destination_id>', methods=['POST'])
def delete_destination(destination_id):
    # Check if the user is authenticated
    if not current_user.is_authenticated:
        flash('You need to log in to delete destinations.', 'danger')
        return redirect(url_for('login'))

    # Retrieve the destination by ID
    destination = Destination.query.get_or_404(destination_id)

    # Check if the current user is the creator
    if current_user.id != destination.user_id:
        flash('You are not authorized to delete this destination.', 'danger')
        return redirect(url_for('explore'))

    # Delete the destination from the database
    db.session.delete(destination)
    db.session.commit()

    flash('Destination deleted successfully!', 'success')
    return redirect(url_for('explore'))



def save_destination_image(image):
    # Handle the image upload, save it to a folder or cloud storage
    # For now, save it to the 'static/images/destinations' folder
    destination_images_folder = os.path.join(app.root_path, 'static', 'images', 'destinations')
    
    # Ensure the folder exists
    os.makedirs(destination_images_folder, exist_ok=True)

    # Generate a unique filename
    filename = secrets.token_hex(8) + secure_filename(image.filename)

    # Save the file to the destination folder
    image_path = os.path.join('images', 'destinations', filename)
    image.save(os.path.join(app.root_path, 'static', image_path))

    return 'static/' + image_path  # Include 'static/' in the path 

#hadnling login --------------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            #flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html'  )

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))  # Redirected to login page

#-Reset passwork --------------------------
# Handling password reset request
@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    form = ResetPasswordRequestForm()

    if form.validate_on_submit():
        # Check if the email exists in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            # Generate a secure token for resetting the password
            token = secrets.token_urlsafe(32)
            user.reset_password_token = token
            db.session.commit()

            # Create a Message object for the email
            msg = Message('Password Reset Request', sender=app.config['MAIL_USERNAME'], recipients=[user.email])
            reset_url = url_for('reset_password_token', token=token, _external=True)
            msg.body = f'To reset your password, click the following link: {reset_url}'

            try:
                # Send the password reset email
                mail.send(msg)
                flash('Password reset instructions sent to your email.', 'success')
            except Exception as e:
                # Log any exceptions
                flash(f'Error sending password reset email: {str(e)}', 'danger')

        else:
            # User with the provided email does not exist
            flash('No account found with that email address.', 'danger')

        return redirect(url_for('login'))

    return render_template('reset_password_request.html', form=form)

# Handling reset link
@app.route('/reset_password_token/<token>', methods=['GET', 'POST'])
def reset_password_token(token):
    # Implement logic to validate the token and handle the password reset
    form = ResetPasswordForm()

    if form.validate_on_submit():
        # Implement logic to update the user's password
        flash('Password reset successful. You can now log in with your new password.', 'success')
        return redirect(url_for('login'))

    return render_template('reset_password.html', form=form)

# ... your existing routes ...

@app.route('/reset_password_request_alternative', methods=['GET', 'POST'])
def reset_password_request_alternative():
    form = ResetPasswordForm()

    if form.validate_on_submit():
        # Implement logic to handle password reset
        # This might involve sending an email with a reset link, etc.
        flash('Password reset instructions sent to your email.', 'success')
        return redirect(url_for('login'))

    return render_template('reset_password.html', form=form)


#--- send email reset message
@app.route('/send_test_email')
def send_test_email():
    # Create a Message object
    msg = Message('Test Email', sender=os.environ.get('MAIL_USERNAME'), recipients=['recipient@example.com'])
    msg.body = 'This is a test email.'

    try:
        # Send the message
        mail.send(msg)
        flash('Test email sent successfully!', 'success')
    except Exception as e:
        # Log any exceptions
        flash(f'Error sending test email: {str(e)}', 'danger')

    return redirect(url_for('home'))  # Redirect to home page or another appropriate route


#----signup part --------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    
    form = SignupForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Check if the username or email is already taken
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('Username or email already exists. Please choose a different one.', 'danger')
        else:
            # Create a new user and add it to the database
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()

            flash('Account created successfully! You can now log in.', 'success')

            # Automatically log in the new user
            login_user(new_user)

            return redirect(url_for('home'))

    return render_template('signup.html', form=form )
#=======================



@app.route('/search', methods=['POST'])
def search():
    # Retrieve the search query from the form
    search_query = request.form.get('search')

    # TODO: Implement the logic to search for destinations based on the query
    # You might want to query your database for matching destinations

    # For now, let's assume you have a list of destinations
    # Replace this with your actual logic
    destinations = [
        {'name': 'Destination 1', 'location': 'Location 1', 'photo': 'photo1.jpg'},
        {'name': 'Destination 2', 'location': 'Location 2', 'photo': 'photo2.jpg'},
        # ...
    ]

    return render_template('search_results.html', query=search_query, destinations=destinations)



###to add contents for homepage 
@app.route('/add_travel_package', methods=['GET', 'POST'])
def add_travel_package():
    form = AddTravelPackageForm()
    travel_packages = TravelPackage.query.all()
    if form.validate_on_submit():
        print('form validate data ')
        # Retrieve data from the form
        new_package_name = form.name.data
        new_package_description = form.description.data
        new_package_location = form.location.data
        new_package_hotel = form.hotel.data
        new_package_hetel_des = form.hotel_description.data
        new_package_duration = form.duration.data
        new_package_package_price = form.package_price.data
        new_package_latitude = form.latitude.data
        new_package_longitude = form.longitude.data
        
        # Create a new TravelPackage object and add it to the database
        new_package = TravelPackage(
            name=new_package_name,
            description=new_package_description,
            location=new_package_location,
            hotel=new_package_hotel,
            hotel_description=new_package_hetel_des,
            duration= new_package_duration,
            package_price = new_package_package_price,
            latitude=new_package_latitude,
            longitude=new_package_longitude
           
        )

        db.session.add(new_package)
        db.session.commit()

        # Save the uploaded images and associate them with the new package
        for i in range(1, 4):  # Assuming three images
            image_key = f'image{i}'
            image_file = getattr(form, image_key).data

            if image_file:
                image_path = save_travel_package_image(image_file)
                new_image = TravelPackageImage(
                    filename=image_path,
                    travel_package_id=new_package.id
                )

                db.session.add(new_image)

        db.session.commit()

        flash('Travel package added successfully!', 'success')
        #return redirect(url_for('add_travel_package.html'))  # Redirect to the explore page or another appropriate route
        return render_template('add_travel_package.html', form=form, travel_packages=travel_packages)
    travel_packages = TravelPackage.query.all()
    return render_template('add_travel_package.html', form=form,travel_packages=travel_packages)

def save_travel_package_image(image):
    # Handle the image upload and save it to a folder
    package_images_folder = os.path.join(current_app.root_path, 'static', 'images', 'travel_packages')

    # Ensure the folder exists
    os.makedirs(package_images_folder, exist_ok=True)

    # Generate a unique filename
    filename = secrets.token_hex(8) + secure_filename(image.filename)

    # Save the file to the package images folder
    image_path = os.path.join('images', 'travel_packages', filename)
    image.save(os.path.join(current_app.root_path, 'static', image_path))

    return '/static/' + image_path