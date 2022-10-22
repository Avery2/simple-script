from flask import Flask, request, render_template, g, init_db

app = Flask(__name__)


output_anchor = '<!-- output anchor -->'
sum_anchor = '<!-- sum anchor -->'
g.acc_sum = 0


def create_app():
    app = Flask(__name__)

    with app.app_context():
        init_db()

    return app


@app.route('/')
def my_form():
    return flask_print('')


@app.route('/', methods=['POST'])
def my_form_post():
    text = get_flask_input()

    if (text.isnumeric()):
        g.acc_sum += int(text)

    return flask_print(text)


def get_flask_input():
    return request.form['text']


def flask_print(text):
    return render_template('my-form.html').replace(output_anchor, text).replace(sum_anchor, f'sum: {g.acc_sum}')
