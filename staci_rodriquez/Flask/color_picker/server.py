from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'mypasswordizmypa$$w0rd'

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/color', methods=['POST'])
def colors():
    red = (request.form['red'])
    if red != "":
        red = int(red)

    green = (request.form['green'])
    if green != "":
        green = int(green)

    blue = (request.form['blue'])
    if blue != "":
        blue = int(blue)

    error = False

    if red < 1 or red > 255:
        flash("Red value must be between 1 and 255")
        error = True

    if green < 1 or green > 255:
        flash("Green value must be between 1 and 255")
        error = True

    if blue < 1 or blue > 255:
        flash("Blue value must be between 1 and 255")
        error = True

    if error:
        return redirect('/')
    return render_template('index.html', red=red, green=green, blue=blue)

app.run(debug=True)