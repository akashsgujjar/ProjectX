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


def addToDatabase(username, email):

    data = {"name": username,
            "email": email}
    db.child("users").child("User: " + username).set(data)

    users = db.child("users").get()
    print(users.val())


@app.route('/addRegion', methods=['POST'])
def addRegion():
    username = request.form['username']
    email = request.form['email']

    addToDatabase(username ,email)
    return render_template('index.html', name=username)

# export FLASK_APP=bot.py
# flask run
