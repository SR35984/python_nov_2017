from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation')
app.secret_key = 'some_secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-0\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    query  = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def check():
    errors = []
    email = request.form['email']

    if len(email) == 0:
        errors.append("Email is required.")
        flash (errors)

    elif not EMAIL_REGEX.match(email):
        errors.append("Not a valid email!")
        flash (errors)

    query = "SELECT * FROM users"
    data = {'email': request.form['email']}
    results = mysql.query_db(query, data)

    if len(results) == results:
        errors.append("Email already taken")
        flash (errors)

    if len(errors) > 0:
        return redirect('/')
    else:
        flash("The email address you entered " + email + " is a VALID email address! Thank you!")

        # insert the new email to the db
        query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW() )"
        data = {'email': request.form['email']}
        print email
        mysql.query_db(query,data) # Need to pass data as second arguement (mysqlconnection.py line#25)

        # select query for all the emails
        query = "SELECT * FROM users ORDER BY id DESC"
        users = mysql.query_db(query)
        return render_template('success.html', users = users)

app.run(debug=True)