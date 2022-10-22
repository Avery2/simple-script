from flask import Flask, request, render_template

app = Flask(__name__)


anchor = '<!-- output anchor -->'


@app.route('/')
def my_form():
    return flask_print('')


@app.route('/', methods=['POST'])
def my_form_post():
    text = get_flask_input()

    return flask_print(text)


def get_flask_input():
    return request.form['text']


def flask_print(text):
    return render_template('my-form.html').replace(anchor, text)
