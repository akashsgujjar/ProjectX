from flask import Flask, flash, jsonify, render_template, request
import webbrowser
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
    return render_template('index.html', name="hello")


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
            if username == userDataValues["name"]:
                return render_template('profile.html', name="login success you are " + userDataValues["email"])
        return render_template('login.html', name=None)
    if request.method == 'GET':
        return render_template('login.html', name=None)
    else:
        return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    year = request.form['year']
    person = addToDatabase(username, email, year)
    return profile(person)


@app.route('/profilePage')
def profile(person):
    users = db.child("users").child(person).get()
    temp = users.val()
    return render_template('login.html', name=temp)


def addToDatabase(username, email, year):
    data = {"name": username,
            "email": email,
            "year": year}
    person = "User: " + username
    db.child("users").child(person).set(data)
    users = db.child("users").get()
    return person

# FLASK_APP=bot.py FLASK_ENV=development flask run
