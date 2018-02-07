from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")


@app.route('/ninjas')
def ninjas():
  return render_template("ninjas.html")

@app.route('/dojo/new')
def new_dojo():
	return render_template("dojos.html")

app.run(debug=True) # run our server