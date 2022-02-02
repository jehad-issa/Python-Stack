from ast import Num
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/say/<jehad>')
def name(jehad):
    return 'hi '+jehad

@app.route('/repeat/<int:num>/<name>')
def repeat(num,name):

    return name*num

if __name__=="__main__":    
    app.run(debug=True) 

 