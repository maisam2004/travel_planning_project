from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user, logout_user, login_required
from travel_planning import app,db,login_manager
from .models import User
from .forms import SignupForm , ResetPasswordForm,ResetPasswordRequestForm
from flask_mail import Message
from . import mail
import os
import secrets 
#from travel_planning.models import Category , Task

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/explore')
def explore(): #Destination Management
    return render_template('explore.html')

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
    return render_template('login.html')

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

    return render_template('signup.html', form=form)
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


@app.route("/list_holidays")
def list_holidays():
  return "Holidays and observances"

