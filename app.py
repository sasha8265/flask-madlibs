from flask import Flask, request, render_template


app = Flask(__name__)

app.config['SECRET_KEY'] = "sashacandoit"

@app.route('/')
def form_home():
    return render_template("form.html")


@app.route('/story')
def show_story():



    return render_template("story.html")

