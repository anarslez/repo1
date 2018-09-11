from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)    
print(__name__)
app.secret_key = 'dsfksdjfk' 
@app.route('/')
def index():
    return render_template("login.html")
@app.route('/user', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['lang'] = request.form['lang']
    session['loc'] = request.form['loc']
    session['email'] = request.form['email']
    session['comment'] = request.form['comment']
    if len(session['email']) < 1:
        flash("Email cannot be blank!", session['email'])
    elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Address!", session['email'])
    if len(session['comment']) < 1:
        flash("Comment cannot be blank!", session['comment'])
    elif len(session['comment']) > 100:
        flash("Comment must be less than 100 characters", session['comment'])

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return redirect('/result')
@app.route('/result')
def show():
    comment = session['comment']
    loc = session['loc']
    lang = session['lang']
    return render_template("show.html", loc = loc, lang = lang, comment = comment)
if __name__=="__main__":   
    app.run(debug=True)