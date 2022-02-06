from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def creat_form():
    return render_template("creat_form.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    Language_from_form = request.form['Language']
    Comment_from_form = request.form['Comment']

    return render_template("show.html", name_on_template=name_from_form, location_on_template=location_from_form,Language_on_template=Language_from_form,
        Comment_on_template=Comment_from_form)    

if __name__ == "__main__":
    app.run(debug=True)