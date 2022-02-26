from flask import Flask, request, render_template, jsonify
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = "sashacandoit"


@app.route('/')
def form_home():
    """Generate form page and populate input labels with prompts"""
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)


@app.route('/story')
def show_story():

    # all_args = dict(request.args)
    # answers = jsonify(all_args)

    text = story.generate(request.args)

    return render_template("story.html", text=text)

