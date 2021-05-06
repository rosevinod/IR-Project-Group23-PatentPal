from flask import Flask, render_template, url_for, redirect, request
# import summary
import retrieval_lib


app = Flask(__name__)

def clean_text(text):
    text = text.replace(" .", ".")
    text = text.replace(" ,", ",")
    text = text.replace(" )", ")")
    text = text.replace("( ", "(")
    text = text.replace(" ;", ";")
    text = text.strip()
    newtext = list(text[0].upper() + text[1:])

    for i in range(len(text)):
        if i < len(text)-2:
            if text[i] == ".":
                newtext[i+2] = newtext[i+2].upper()

    return "".join(newtext)


def get_results(search_query):
    if search_query != "":
        outputs = retrieval_lib.retrieve_patents(search_query)

        for i in outputs:
            i[2] = clean_text(i[2])
            upd = i[2][:500]

            if upd != i[2]:
                upd = upd + "..."

            i[2] = upd
            i[3] = clean_text(i[3])

        return outputs
    return None

@app.route("/", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def home():
    return render_template("home_page.html")

@app.route("/retrieval", methods = ['GET', 'POST'])
def retrieval():
    search_query = request.form.get("search_box")
    print(search_query)
    if request.method == "POST":
        results =  get_results(search_query)
        if results is not None:
            return render_template("retrieval_page.html", show_hidden = True, search_query = search_query, len = 10, outputs = results)

    return render_template("retrieval_page.html", show_hidden = False)

@app.route("/summarise", methods = ['GET', 'POST'])
def summarise():
    if request.form.get("Clear_Button"):
        return render_template("summary_page.html", show_hidden = False)

    if request.method == "POST":
        input_text = request.form.get("input_patent")
        if input_text != "":
            output_text = "abcd  hello"
            # output_text = summary.get_summary(input_text)
            return render_template("summary_page.html", show_hidden = True, input_text = input_text, output_text = output_text)

    return render_template("summary_page.html", show_hidden = False)


if __name__ == "__main__":
    app.run(debug = True)
