from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)    
print(__name__)
app.secret_key = 'dsfksdjfk'
@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = 1
    else:
        session['num'] = session['num']+1
    return render_template("count.html", num = int(session['num']))
@app.route('/one', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    return redirect('/')
@app.route('/two', methods=['GET'])
def create_user2():
    session['num'] = session['num']+1
    return redirect('/')
@app.route('/three', methods=['GET'])
def create_user3():
    session['num'] = 0
    return redirect('/')
if __name__=="__main__":   
    app.run(debug=True)