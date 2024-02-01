from flask import render_template,redirect,request,url_for
from travel_planning import app,db
#from travel_planning.models import Category , Task

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/explore')
def explore(): #Destination Management
    return render_template('explore.html')

@app.route('/login')
def login():

    return render_template('login.html')

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