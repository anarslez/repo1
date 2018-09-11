from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)    
print(__name__)
app.secret_key = 'dsfksdjfk' 
@app.route('/')
def index():
    return render_template("register.html")
@app.route('/user', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['email'] = request.form['email']
    session['passw'] = request.form['passw']
    session['conpass'] = request.form['conpass']
    if len(session['email']) < 1:
        flash("Email cannot be blank!", session['email'])
    elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Address!", session['email'])
    if len(session['fname']) < 1:
        flash("First name cannot be blank!", session['fname'])
    if any(i.isdigit() for i in session['fname']):
        flash("Your first name does not contain a number you weirdo!", session['fname'])
    if len(session['lname']) < 1:
        flash("Last name cannot be blank!", session['lname'])
    if any(i.isdigit() for i in session['lname']):
        flash("Your last name does not contain a number you weirdo!", session['lname'])
    if len(session['passw']) < 8:
        flash("Password cannot be blank!", session['passw'])
    if session['conpass'] != session['passw']:
        flash("Passwords must match!", session['conpass'])

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return redirect('/result')
@app.route('/result')
def show():
    fname = session['fname']
    lname = session['lname']
    email = session['email']
    passw = session['passw']
    conpass = session['conpass']
    return render_template("result.html", email = email, fname = fname, lname = lname, passw = passw, conpass = conpass)
if __name__=="__main__":   
    app.run(debug=True)