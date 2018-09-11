from flask import Flask, render_template 
app = Flask(__name__)    
print(__name__)          
@app.route('/<x>/<y>')          
def play(x,y):
    return render_template("checkers.html", x = int(x), y = int(y), num = float(100/int(x)-4))
if __name__=="__main__":   
    app.run(debug=True)  
