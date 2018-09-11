from flask import Flask, render_template, request, redirect, session, flash
# import the function connectToMySQL from the file mysqlconnection.pycopy
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'dsfksdjfk'

@app.route('/')
def index():
    mysql = connectToMySQL("piechartdb")
    all_order = mysql.query_db("SELECT * FROM orders")
    print("Fetched all orders", all_order)
    return render_template('piechart.html', orders = all_order)

@app.route('/create', methods=['POST'])
def create():
    mysql = connectToMySQL("piechartdb")
    query = "INSERT INTO orders (name, orders, created_at, updated_at) VALUES (%(name)s, %(orders)s, NOW(), NOW());"
    data = {
             'name': request.form['name'],
             'orders':  int(request.form['orders'])
           }
    new_friend_id = mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__": 
    app.run(debug=True)