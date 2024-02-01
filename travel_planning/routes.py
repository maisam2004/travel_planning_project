from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user, logout_user, login_required
from travel_planning import app,db,login_manager
from .models import User

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
            flash('Logged in successfully!', 'success')
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

#-----------------------------------------
#----signup part --------------


@app.route('/signup')
def signup():
    return render_template('signup.html')



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

