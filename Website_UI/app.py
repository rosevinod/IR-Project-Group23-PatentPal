from flask import Flask, render_template, url_for, redirect, request
import summary
import random

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
	if request.form.get("Clear_Button"):
		return render_template("summary_page.html", show_hidden = False)

	if request.method == "POST":
		input_text = request.form.get("input_patent")
		# print(input_text)
		if input_text != "":
			output_text = summary.get_summary(input_text)
			# output_text = "abcd" + str(random.randint(1, 100))
			return render_template("summary_page.html", show_hidden = True, input_text = input_text, output_text = output_text)

	return render_template("summary_page.html", show_hidden = False)


if __name__ == "__main__":
	app.run(debug = True)
