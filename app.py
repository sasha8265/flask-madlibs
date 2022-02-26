from flask import Flask, request, render_template
from stories import story1


app = Flask(__name__)
app.config['SECRET_KEY'] = "sashacandoit"


@app.route('/')
def form_home():
    """Generate form page and populate input labels with prompts"""
    prompts = story1.prompts
    return render_template("form.html", prompts=prompts)


@app.route('/story')
def show_story():

    text = story1.generate(request.args)

    return render_template("story.html", text=text)