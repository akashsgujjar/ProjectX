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


@app.route('/addRegion', methods=['POST'])
def addRegion():
    username = request.form['username']
    email = request.form['email']
    year = request.form['year']
    addToDatabase(username, email, year)
    return render_template('index.html', name=username)


def addToDatabase(username, email, year):
    data = {"name": username,
            "email": email,
            "year": year}
    db.child("users").child("User: " + username).set(data)

    users = db.child("users").get()
    print(users.val())

# export FLASK_APP=bot.py
# flask run
