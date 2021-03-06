from flask import Flask, render_template, request, redirect, session, flash, url_for
app = Flask(__name__)
app.secret_key = 'mypasswordizmypa$$w0rd'


@app.route('/')
def index():
    return render_template('dn_index.html') 

@app.route('/ninja')
def ninja():
    if ('myKey' not in session) or ('myKey' in session):
        session['myKey'] = 'hello'
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def show_ninja(color):
    if 'myKey' in session:
        session.pop('myKey')
    return render_template('ninja.html', color = color)

app.run(debug=True)