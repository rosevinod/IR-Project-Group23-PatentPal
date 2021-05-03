from flask import Flask, render_template, url_for, redirect


app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def home():
	return render_template("home_page.html")

@app.route("/retrieval", methods = ['GET', 'POST'])
def retrieval():
	print("page fetched!!!")
	return render_template("retrieval_page.html")

@app.route("/summarise", methods = ['GET', 'POST'])
def summarise():
	return render_template("summary_page.html")


if __name__ == "__main__":
	app.run(debug = True)
