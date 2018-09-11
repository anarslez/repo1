from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)    
print(__name__)
app.secret_key = 'dsfksdjfk'
@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    if 'message' not in session:
        session['message'] = ''
    context = {
                'word' : request.POST['word'],
                'color' : request.POST['color'],
                'big_font' : int(showbig),
            }
    return render_template("ninjagold.html", count = int(session['count']), message = session['message'])

@app.route('/process', methods=['POST'])
def create_instance():
    print(request.form)
    if request.form['action'] == 'farm':
        session['count'] = session['count']+random.randrange(10,20)
        session['message'] = session['message']+'Where did you find '+str(session['count'])+' gold on a farm. '
    elif request.form['action'] == 'cave':
        session['count'] = session['count']+random.randrange(5,10)
        session['message'] = session['message']+'Where did you find '+str(session['count'])+' gold in a cave. '
    elif request.form['action'] == 'house':
        session['count'] = session['count']+random.randrange(2,5)
        session['message'] = session['message']+'Where did you find '+str(session['count'])+' gold in a house. '
    elif request.form['action'] == 'casino':
        session['count'] = session['count']+50-random.randrange(0,100)
        session['message'] = session['message']+'Where did you find '+str(session['count'])+' gold in a casino. '
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)