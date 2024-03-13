from flask import render_template,redirect,request,url_for,flash,current_app,jsonify,session
from flask_login import login_user, logout_user, login_required,current_user
from travel_planning import app,db,login_manager
from .models import User,Destination,TravelPackage,TravelPackageImage,WishedHoliday,UserImage,UsersCallbackRequest
from .forms import SignupForm , ResetPasswordForm,ResetPasswordRequestForm,AddDestinationForm,EditDestinationForm,AddTravelPackageForm,WishedHolidayForm,UserImageForm,CallbackRequestForm
import phonenumbers
from . import Mail,Message,mail
import os
import re
import secrets 
from werkzeug.utils import secure_filename
import logging
from datetime import datetime, timedelta


@app.route('/', methods=['POST', 'GET'])
def home():
    """Renders the home page, handles form submissions, and displays travel packages.

     This route serves the main functionality of the home page:
        - Retrieves all travel packages for display.
        - Initializes forms for wished holiday submission and callback requests.
        - Handles form submissions:
            - Checks which form was submitted using request.form.
            - Validates and processes the submitted form.
            - Displays success or error flash messages based on the outcome.
        - Renders the 'home.html' template with:
            - All travel packages.
            - The wished holiday form.
            - The callback request form.

    Returns:
        Rendered 'home.html' template with travel packages and forms.
    """

    travel_packages = TravelPackage.query.all()
    # Initialize the forms
    callback_request_form = CallbackRequestForm()
    wished_holiday_form = WishedHolidayForm()
    wished_holiday_errors = []
    callback_request_errors = []

    # Check which form was submitted (and potentially show success message)
    submitted_form:bool = None
    
    

    if 'wished_holiday-submit' in request.form:
    # Handle wished holiday form submission
        submitted_form = wished_holiday_form
        if wished_holiday_form.validate_on_submit():
            wished_holiday = WishedHoliday(
                holiday_type=wished_holiday_form.holiday_type.data,
                travel_duration=wished_holiday_form.travel_duration.data,
                price_range=wished_holiday_form.price_range.data,  # Include price_range field
                travel_time=wished_holiday_form.travel_time.data,
                departure_location=wished_holiday_form.departure_location.data,
                additional_info=wished_holiday_form.additional_info.data,
                user_id=current_user.id  # Ensure current_user is correct
            )
            db.session.add(wished_holiday)
            try:
                db.session.commit()
                flash('Your wished holiday has been submitted successfully!', 'success')
                # Redirect to home page after successful submission (optional)
                return redirect(url_for('wished_holiday'))
            except Exception as e:
                logging.error(f"Error saving wished holiday: {e}")
                flash('An error occurred while submitting your wish.', 'danger')

   
    
    #if callback_request_form.validate_on_submit():
    elif 'callback_request-submit' in request.form:
        print("Callback part for submit only not validate")
        submitted_form=callback_request_form
        if callback_request_form.validate_on_submit():
        # Handle callback request form submission (similar to wished_holiday)
            callback_request = UsersCallbackRequest(
                name=callback_request_form.name.data.strip(),
                phone=callback_request_form.phone.data.strip(),
                package_name=callback_request_form.package_name.data.strip(),
                message=callback_request_form.message.data.strip()
            )
            db.session.add(callback_request)
            try:
                db.session.commit()
                flash('Your call request submitted successfully, we will contact you shortly', 'success')
                
            except phonenumbers.phonenumberutil.NumberParseException:
                flash('Please enter a valid phone number.', 'danger')
            except Exception as e:
                logging.error(f"Error saving callback request: {e}")
                flash('An error occurred while submitting your request.', 'danger')
    if submitted_form:
        if not submitted_form.validate_on_submit():
            for field, errors in submitted_form.errors.items():
                for error in errors:
                    wished_holiday_errors.append(f"{field.capitalize()}: {error}")

    # Collect errors after handling submission (if any)
    #wished_holiday_errors = wished_holiday_form.errors.copy()
    #callback_request_errors = callback_request_form.errors.copy()

# Combine all errors
    all_errors = wished_holiday_errors.copy()
    all_errors.extend(callback_request_errors)

    return render_template('home.html',
                        travel_packages=travel_packages,
                        wished_holiday_form=wished_holiday_form,
                        callback_request_form=callback_request_form,
                        #wished_holiday_errors=wished_holiday_errors,
                        #callback_request_errors=callback_request_errors,
                        all_errors=all_errors)

#################################################



@app.route('/wished_holiday')
@login_required
def wished_holiday():
    """Displays a user's submitted wished holidays.

    This route retrieves all wished holidays for the currently logged-in user 
    from the database and renders them on the 'wished_holiday.html' template.

    Returns:
        Rendered 'wished_holiday.html' template with the user's wished holidays.
    """
    wishes = WishedHoliday.query.filter_by(user_id=current_user.id).all()
    last_wish = WishedHoliday.query.filter_by(user_id=current_user.id).order_by(WishedHoliday.id.desc()).first()

    return render_template('wished_holiday.html', wishes=last_wish) 



#delete wished holiday =============
@app.route('/account/delete/<int:wishedholiday_id>', methods=['POST'])
@login_required
def delete_wished(wishedholiday_id):
    """Deletes a wished holiday for the logged-in user.

    This route retrieves a wished holiday by its ID, checks if it belongs to 
    the current user, and then deletes it from the database. If successful, a 
    success flash message is displayed, and the user is redirected to the 
    account page.

    Args:
        wishedholiday_id (int): ID of the wished holiday to delete.

    Returns:
        Redirects to the account page with a success flash message on success.
        Returns a 404 error if the wished holiday is not found.
    """

    wished = WishedHoliday.query.get_or_404(wishedholiday_id)


    # Delete the destination from the database
    db.session.delete(wished)
    db.session.commit()

    flash('Destination deleted successfully!', 'success')
    return redirect(url_for('account'))



# route for contact_us page
@app.route('/contact_us')
def contact_us():
    """This is to hadle contact page """
    
    return render_template('contact_us.html'  )





@app.route('/about', methods=['POST','GET'])
def about():
    """Render the about page."""
    
    return render_template('about_us.html' )





@app.route('/explore', methods=['GET', 'POST'])
def explore():
    """Shows a list of destinations and allows adding new ones (if logged in).

    This route handles both GET and POST requests for the explore page. It displays 
    a list of all destinations (public or user's own if logged in) and provides 
    a form for adding new destinations (for authenticated users only).

    Returns:
        Rendered 'explore.html' template with a list of destinations and an 
        optional add destination form if the user is logged in.
    """
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
        return render_template('explore.html', form=form,all_destinations=all_destinations)
        #return render_template('explore.html', form=form, user_destinations=user_destinations)

    else:
        # User is not logged in, only allow viewing
        
        all_destinations = Destination.query.all()
    return render_template('explore.html', form=form,all_destinations=all_destinations )





## edit  destination -----------------

@app.route('/explore/edit/<int:destination_id>', methods=['GET', 'POST'])
def edit_destination(destination_id):
    """Edits a user's own destination (authenticated users only).

    Allows editing destination details and saving changes.

    Args:
        destination_id (int): ID of the destination to edit.

    Returns:
        - Redirects on success/failure (with flash messages).
        - Renders edit form on GET or invalid form submission.
    """
    
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
    """Deletes a destination (authenticated users only).

    Allows authenticated users to delete their own destinations.

    Args:
        destination_id (int): ID of the destination to delete.

    Returns:
        - Redirects to explore page with success message on success.
        - Redirects to login page with error message if not authenticated.
        - Redirects to explore page with error message if not authorized.
    """
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
    """Saves a destination image to a designated folder.

    This function handles uploading a destination image, generates a unique 
    filename, and saves it to the 'static/images/destinations' folder within 
    the application's root directory.

    Args:
        image (werkzeug.datastructures.FileStorage): The image file object 
            uploaded by the user.

    Returns:
        str: The relative path (including 'static/') of the saved image file.

    Raises:
        OSError: If an error occurs while creating the destination folder.
    """
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
    """Retrieves a user by ID for login purposes.

    This callback function is used by Flask-Login to retrieve a user object 
    based on the provided user ID. It queries the database for a User record 
    matching the ID and returns it, allowing Flask-Login to handle user 
    session management.

    Args:
        user_id (str): User ID to retrieve.

    Returns:
        User: The retrieved user object if found, otherwise None.
    """
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user login requests.

    This route processes login attempts. On a GET request, it renders the 
    login form. On a POST request, it retrieves username and password from the 
    form data, validates them against the database, and logs in the user on 
    success. If login fails, an error flash message is displayed.

    Returns:
        - Rendered 'login.html' template on GET request.
        - Redirected to the home page with a success flash message on successful 
          login.
        - Rendered 'login.html' template again with an error flash message on 
          failed login attempt.
    """
    
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
    """Logs out the currently authenticated user.

    This route handles user logout requests. It logs out the current user 
    using Flask-Login and displays a success flash message. The user is then 
    redirected to the login page.

    Returns:
        Redirected to the login page with a success flash message.
    """
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))  # Redirected to login page

#-Reset passwork --------------------------
# Handling password reset request
@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    """Initiates password reset process by email.

    This route handles the initial password reset request:
      - Renders a form for users to enter their email address.
      - On valid form submission:
         - Checks for a user with the given email.
         - Generates a secure reset token and assigns it to the user.and secssion 
         - Sends an email with a password reset link containing the token.
         - Redirects to the login page with a success message.
      - On email not found or email sending failure:
         - Displays an appropriate error flash message.
         - Redirects to the login page.

    Returns:
        - Rendered 'reset_password_request.html' template with form on GET.
        - Redirected to login page with success/error message on POST.
    """
    form = ResetPasswordRequestForm()

    if form.validate_on_submit():
        # Check if the email exists in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            # Generate a secure token for resetting the password
            token = secrets.token_urlsafe(32)
            session['reset_password_token'] = token
            session['reset_password_token_expiration'] = datetime.now() + timedelta(minutes=15)
            

            # Create a Message object for the email
            msg = Message('Password Reset Request at Travel-app', sender=app.config['MAIL_USERNAME'], recipients=[user.email],html=True)
            reset_url = url_for('reset_password_token', token=token, _external=True)
            
            #msg.body = f'To reset your password, click the following link: {reset_url}'
            msg.html = f"""
                            <!DOCTYPE html>
                            <html>
                            <head>
                                <meta charset="UTF-8">
                                <title>Password Reset Request</title>
                                <style>
                                    body {{
                                        font-family: sans-serif;
                                    }}
                                    .button {{
                                        background-color: #007bff; /* Blue color */
                                        border-radius:50%;
                                        color: white;
                                        padding: 10px 20px;
                                        text-decoration: none;
                                        border-radius: 5px;
                                        display: inline-block;
                                    }}
                                </style>
                            </head>
                            <body>
                                <h2>Password Reset Request</h2>
                                <p>Hi {user.username},</p>
                                <p>You recently requested to reset your password for your account.</p>
                                <p>To proceed with resetting your password in the next 15 minutes, please click the button below:</p>
                                <a href="{reset_url}" class="button">Reset Password</a>
                                <p>If you didn't make this request, please ignore this email.</p>
                                <p>Thanks,<br>Travel App Team</p>
                            </body>
                            </html>
                            """   
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
from datetime import datetime

@app.route('/reset_password_token/<token>', methods=['GET', 'POST'])
def reset_password_token(token):
    """
    Allows resetting a password using a valid reset token.

    This route handles password reset requests using a token typically sent 
    via email. It retrieves a user based on the token (replace `User.query.get(1)` 
    with your token validation logic) and renders a form to set a new password. 
    On a valid form submission, it updates the user's password and redirects to 
    the login page with a success message.

    Args:
        token (str): The password reset token from the email link.

    Returns:
        - Rendered 'reset_password.html' template with a form on GET request.
        - Redirected to the login page with a success flash message on successful 
          password reset.
    """

    # User and token are valid
     # User and token are valid
    form = ResetPasswordForm()

    if form.validate_on_submit():
        # Update the user's password
        user = User.query.get(1)  
        user.set_password(form.password.data)  # Use bcrypt for secure hashing
        db.session.commit()

        flash('Password reset successful. You can now log in with your new password.', 'success')
        return redirect(url_for('login'))

    # Check if the reset token is valid and has not expired
    if 'reset_password_token' in session and 'reset_password_token_expiration' in session:
        if session['reset_password_token'] == token and session['reset_password_token_expiration'].replace(tzinfo=None) > datetime.now():
            # Token is valid and has not expired
            return render_template('reset_password.html', form=form)

    # Token is invalid or has expired
    flash('Invalid or expired password reset token.', 'danger')
    return redirect(url_for('login'))
# ... your existing routes ...

@app.route('/reset_password_request_alternative', methods=['GET', 'POST'])
def reset_password_request_alternative():
    """Initiates the password reset process (alternative method).

    This route handles the initial step of password reset (implementation 
    details might differ from the token-based approach). It renders a form 
    where users can enter their email or username. On form submission 
    (replace with your actual logic), it potentially sends a reset link or 
    instructions via email and redirects to the login page with a success 
    message.

    Returns:
        - Rendered 'reset_password.html' template with a form on GET request.
        - Redirected to the login page with a success flash message indicating 
          reset instructions were sent (replace with actual behavior).
    """

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
    """ Create a test for email  """ 
    msg = Message('Test Email', sender=os.environ.get('MAIL_USERNAME'), recipients=['recipient@example.com'])
    msg.body = 'This is a test email.'

    try:
        # Send the message
        Mail.send(msg)
        flash('Test email sent successfully!', 'success')
    except Exception as e:
        # Log any exceptions
        flash(f'Error sending test email: {str(e)}', 'danger')

    return redirect(url_for('home'))  # Redirect to home page or another appropriate route


#----signup part --------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Processes user signup and logs in on success.

    Renders signup form, validates data, creates new users, 
    and redirects on success or displays errors.

    Returns:
        Rendered signup form or redirects based on success/failure.
    """
    
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


#for practic code not used here 
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


#liked destinations 

@app.route('/like', methods=['POST'])
def like_destination():
    """This is for liked holiday .has not been used for last edited code"""
    destination_id = request.form['destination_id']  #  the destination ID
    destination = Destination.query.get(destination_id)
    if destination:
        # Increment the likes count
        destination.likes += 1
        db.session.commit()
        return jsonify({'success': True, 'likes': destination.likes})
    else:
        return jsonify({'success': False, 'error': 'Destination not found'})





###to add contents for homepage 
@app.route('/add_travel_package', methods=['GET', 'POST'])
def add_travel_package():
    """Handle data porovided for travel packages an show in home """
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
    """Handle the image upload and save it to a folder"""
    
    package_images_folder = os.path.join(current_app.root_path, 'static', 'images', 'travel_packages')

    # Ensure the folder exists
    os.makedirs(package_images_folder, exist_ok=True)

    # Generate a unique filename
    filename = secrets.token_hex(8) + secure_filename(image.filename)

    # Save the file to the package images folder
    image_path = os.path.join('images', 'travel_packages', filename)
    image.save(os.path.join(current_app.root_path, 'static', image_path))

    return '/static/' + image_path


@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for handling 400 Bad Request errors.

    Args:
        e (Exception): The exception object representing the error.

    Returns:
        str: A user-friendly message indicating a bad request.
    """

    return "Page not found. Please check the URL.", 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom error handler for handling 500 Internal Server Error.

    Args:
        e (Exception): The exception object representing the error.

    Returns:
        str: A user-friendly message indicating an internal server error.
    """

    return render_template("error.html"), 500



@app.route('/callback_requests', methods=['GET'])
def callback_requests():
    """ Retrieve all callback requests from the database"""
    callback_requests = UsersCallbackRequest.query.all()
    return render_template('callback_requests.html', callback_requests=callback_requests)



##
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    """Render the user account page and handle profile image uploads."""
    
    # Retrieve wished holidays associated with the current user
    wishes = WishedHoliday.query.filter_by(user_id=current_user.id).all()
    
    # Retrieve user's image if it exists
    user_image = UserImage.query.filter_by(user_id=current_user.id).first()

    # Create form instance
    user_image_form = UserImageForm()

    if user_image_form.validate_on_submit():
        # Save the uploaded image
        image_file = user_image_form.image.data
        filename = secure_filename(image_file.filename)
        filepath = os.path.join(app.root_path, 'static', 'images', filename)
        image_file.save(filepath)

        # Check if user already has an image record
        if user_image:
            # Check if there are backslashes in the filepath and replace them with forward slashes

            user_image.image_path = filepath
        else:
            user_image = UserImage(user_id=current_user.id, image_path=filepath)
            db.session.add(user_image)

        db.session.commit()
        flash('Profile image uploaded successfully!', 'success')
        return redirect(url_for('account'))

    # Pass form, user's image, and wishes to the template
    return render_template('account.html', user=current_user, user_image=user_image, user_image_form=user_image_form, wishes=wishes)