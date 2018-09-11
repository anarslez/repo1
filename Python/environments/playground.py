from flask import Flask, render_template 
app = Flask(__name__)    
print(__name__)          
@app.route('/play')          
def play():
    return render_template("index.html", num = 3)
@app.route('/play/<x>')          
def playx(x):
    return render_template("index.html", num = int(x))
@app.route('/play/<x>/<color>')
def playxc(x,color):
    return render_template("index.html", num = int(x),color = color)
if __name__=="__main__":   
    app.run(debug=True)  