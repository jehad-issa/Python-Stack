from flask import Flask, render_template 

app = Flask(__name__)
@app.route('/')                           
def checkBoard():
    return render_template('cheachboard.html', y = 8, x = 8 )

@app.route('/<x>')
def checkBoard1(x):
    return render_template("cheachboard.html", y = int(x), x = 8)	

@app.route('/<x>/<y>')
def checkBoard2(x, y):
    return render_template("cheachboard.html", y = int(x), x = int(y))	



if __name__=="__main__":
    app.run(debug=True)