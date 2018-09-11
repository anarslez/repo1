from flask import Flask 
app = Flask(__name__)    
print(__name__)          
@app.route('/')          
def hello_world():
    return 'Hello World!'
@app.route('/dojo')          
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def say(name):
    print(name)
    return "hello "+name
@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    print(num)
    print(word)
    return word*int(num)
if __name__=="__main__":   
    app.run(debug=True)  