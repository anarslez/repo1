from flask import Flask, render_template, session, request, redirect, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
bcrypt = Bcrypt(app)
@app.route("/")
def index():
    mysql = connectToMySQL("logindb")
    all_friends = mysql.query_db("SELECT * FROM login")
    print("Fetched all logins", all_friends)
    return render_template("loginregister.html")
   
@app.route("/register", methods=['POST'])
def reserve():
    if len(request.form['first_name']) <= 1:
        flash("First name cannot be blank!", 'first_name')
    if len(request.form['last_name']) <= 1:
        flash("Last name cannot be blank!", 'last_name')
    mysql = connectToMySQL("logindb")
    query = "SELECT * FROM login WHERE email = %(email)s;"
    data = { 'email': request.form['email'] }
    result = mysql.query_db(query, data)
    if len(result)==0:
        if len(request.form['email']) < 1:
            flash("Email cannot be blank!", 'email')
        elif not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!", 'email')
    else:
         flash("Invalid Email Address!", 'email')
    if len(request.form['password']) < 8:
        flash("Password must be 8+ characters!", 'password')
    if request.form['conpassword'] != request.form['password']:
        flash("Passwords must match!", 'conpassword')

    if '_flashes' in session.keys():
        return redirect("/")
    else:
        mysql = connectToMySQL("logindb")
        query = "INSERT INTO login (fist_name, last_name, email, password, created_at, updated_at) VALUES (%(fist_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        data = {
             'fist_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'password': bcrypt.generate_password_hash(request.form['password'])
           }
        new_login_id = mysql.query_db(query, data)
        session['userid'] = new_login_id
        return redirect("/success")
    
@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL("logindb")
    query = "SELECT * FROM login WHERE email = %(email)s;"
    data = { 'email': request.form['email'] }
    result = mysql.query_db(query, data)
    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            session['userid'] = result[0]['id']
            return redirect('/success')
    flash("You could not be logged in", 'login')
    return redirect("/")

@app.route("/success")
def success():
    mysql = connectToMySQL("logindb")
    all_recs = mysql.query_db("SELECT * FROM login")
    data = {'recid' : session['userid']}
    mysql = connectToMySQL("logindb")
    query = "SELECT * FROM messages WHERE messages.rec_id = %(recid)s;"
    all_mess = mysql.query_db(query, data)
    if 'userid' not in session:
        return redirect("/")
    return render_template("registered.html", recs = all_recs, mess = all_mess)

@app.route('/logout', methods=['POST'])
def logout():
    session['userid'] = ''
    return redirect("/")

@app.route('/send', methods=['POST'])
def send():
    mysql = connectToMySQL("logindb")
    query = "INSERT INTO messages (mesage, sent_id, rec_id, created_at, updated_at) VALUES (%(mesage)s, %(sent_id)s, %(rec_id)s, NOW(), NOW());"
    data = {
        'mesage': request.form['message'],
        'sent_id':  session['userid'],
        'rec_id': request.form['rec_id'],
        }
    new_message_id = mysql.query_db(query, data)
    return redirect("/success")

if __name__ == "__main__":
    app.run(debug=True)