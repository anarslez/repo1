from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)    
print(__name__)
app.secret_key = 'dsfksdjfk' 
@app.route('/')
def index():
    return render_template("fruit.html")
@app.route('/buy', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['straw'] = request.form['straw']
    session['app'] = request.form['app']
    session['name'] = request.form['name']
    session['id'] = request.form['id']
    return redirect('/checkout')
@app.route('/checkout')
def show():
    straw = session['straw']
    app = session['app']
    name = session['name']
    id = session['id']
    return render_template("checkout.html", straw = straw, app = app, name = name, id = id, num = int(straw)+int(app))
if __name__=="__main__":   
    app.run(debug=True)