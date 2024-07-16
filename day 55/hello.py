
from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def bold():
        return f"<b>{function()}</b>"
    return bold


def make_underlined(function):
    def bold():
        return f"<u>{function()}</u>"
    return bold
def make_italic(function):
    def italic():
        return f"<em>{function()}</em>"
    return italic


@app.route('/bye')
@make_bold
@make_underlined
@make_italic
def bye():
    return "<h1>AvoieBEJOOaO</h1>"

if __name__ == '__main__':
     app.run(debug=True)