from flask import Flask, flash, jsonify, render_template, request
import webbrowser
from werkzeug.utils import redirect
import firebase as firebase

app = Flask(__name__)
config = {
    "apiKey": "AIzaSyBn6cGqQ8nhyB_nzrm9X9cHhzjfvJW3p44",
    "authDomain": "projectx-51c1b.firebaseapp.com",
    "databaseURL": "https://projectx-51c1b.firebaseio.com",
    "storageBucket": "projectx-51c1b.appspot.com"
}
firebase = firebase.Firebase(config)
db = firebase.database()


@app.route('/')
def handle_data():
    return render_template('index.html', name="Good Afternoon")


@app.route('/login', methods=['POST', "GET"])
def login():
    if request.method == 'POST':
        # gets the username from the html form
        username = request.form['username']
        person = "User: " + username
        users = db.child("users").get()
        # gets a dictionary of all the users in the database
        temp = users.val()
        # gets a list of the usernames from temp
        listOfUsers = temp.keys()
        if person in listOfUsers:
            userData = db.child("users").child(person).get()
            userDataValues = userData.val()
            if username == userDataValues["user"]:
                return redirect('/profilePage')
        return render_template('login.html', name="INVALID ATTEMPT")
    else:
        return render_template('login.html', name=None)


@app.route('/register', methods=['POST'])
def register():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    username = request.form['username']
    email = request.form['email']
    age = request.form['age']
    year = request.form['year']
    person = addToDatabase(firstName, lastName, username, email, age, year)
    return render_template("index.html")


@app.route('/profilePage')
def profile():
    # users = db.child("users").child(person).get()
    # temp = users.val()
    return render_template('profile.html')


@app.route('/matchPage', methods=["GET"])
def match():
    return render_template('match.html')


def addToDatabase(firstName, lastName, username, email, age, year):
    data = {"user": username,
            "first name": firstName,
            "last name": lastName,
            "email": email,
            "age": age,
            "year": year}
    person = "User: " + username
    db.child("users").child(person).set(data)
    users = db.child("users").get()
    return person

# FLASK_APP=auth.py FLASK_ENV=development flask run
