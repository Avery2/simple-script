from flask import Flask, request, render_template

app = Flask(__name__)


output_anchor = '<!-- output anchor -->'
sum_anchor = '<!-- sum anchor -->'
acc_sum = 0


@app.route('/')
def my_form():
    return flask_print('')


@app.route('/', methods=['POST'])
def my_form_post():
    global acc_sum
    text = get_flask_input()

    if (text.isnumeric()):
        acc_sum += int(text)

    return flask_print(text)


def get_flask_input():
    return request.form['text']


def flask_print(text):
    global acc_sum
    return render_template('my-form.html').replace(output_anchor, text).replace(sum_anchor, f'sum: {acc_sum}')
