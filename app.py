from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dopesauze'
debug = DebugToolbarExtension(app)

@app.route('/')
def start():
    return render_template('base.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/form', methods=["POST"])
def form_post():
    place = request.form["place"]
    noun = request.form["noun"]
    verb = request.form["verb"]
    adjective = request.form["adjective"]
    plur = request.form["plural_noun"]
    stories = request.form["stories"]

#     return f"""<h2>Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plur}.</h2>"""

@app.route('/story')
def story():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plur = request.args["plural_noun"]
    stories = request.args["stories"]

    if stories == 'story1':
        return f"""You are in the deep. Found far from the shores of {place}. Sailing accross on a {noun} to find the {adjective} {plur}. But deeper you sank because you were not able to {verb}. The end."""
    elif stories == 'story2':
        return f"""You are in the sand. Blazing heat scorches your back. In the distance you can see {place}--your long awaited destination. But out of the horizon comes a {adjective} {noun}. You {verb}. You try. But you fall into a pit of {plur}. The end."""
    elif stories == 'story3':
        return f"""You are in the sky. You don't know how but faster and faster you fall. You can remember {place} but whether you came from it, you do not know. You remember {adjective} {noun} and being surrounded by {plur}. You remeber how to {verb} and imagine doing so. But you only fall. Further and further. The end. """