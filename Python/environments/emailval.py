from flask import Flask, render_template, request, redirect, session, flash
# import the function connectToMySQL from the file mysqlconnection.pycopy
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'dsfksdjfk'

@app.route('/')
def index():
    if 'color1' not in session:
        session['color1'] = 'white'
    if 'result' not in session:
        session['result'] = ''
    mysql = connectToMySQL("emaildb")
    session['all_email'] = mysql.query_db("SELECT * FROM emails")
    print("Fetched all emails", session['all_email'])
    return render_template('emailval.html', color1 = session['color1'], result = session['result'])

@app.route('/create', methods=['POST'])
def create():
    mysql = connectToMySQL("emaildb")
    if not EMAIL_REGEX.match(request.form['email']):
        session['result'] = 'Invalid Email Address!'
        session['color1'] = 'red'
        return redirect('/')
    else:
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        data = {
             'email': request.form['email']
           }
        new_email_id = mysql.query_db(query, data)
        return redirect('/sucess')

@app.route('/sucess')
def show():
    emails = session['all_email']
    color1 = 'green'
    result = 'You entered a successful email'
    return render_template("sucemail.html", emails = emails, color1 = color1, result = result)

if __name__=="__main__":   
    app.run(debug=True)