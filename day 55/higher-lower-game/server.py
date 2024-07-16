from flask import Flask
from random import randint
the_number = randint(0,9)


app = Flask(__name__)
@app.route('/welcome')
def welcome():
    return ('<h1>Welcome to Higher-Lower Game!</h1>'
            '<h2>Guess a number between 0 and 9</h2>'
            '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif></img>')

@app.route("/regenerated")
def regenerate_number():
    the_number = randint(0, 9)
    print(the_number)
    return '<h1 style="color:blue;">REGENERATED!</h1>'

@app.route("/<int:number>")
def correct(number):
    if number == the_number:
        return (f'<h1 style="color:blue;">Correct! you found me it was {the_number}!</h1>\n'
                f'<a href="/regenerated">Click here to regenerate</a>'
                f'<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif></img>')
    elif number < the_number:
        return (f'<h1 style="color:yellow">Too Low, try again</h1>'
                f'<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif></img>')
    elif number > the_number:
        return (f'<h1 style="color:red">Too High, try again!</h1>'
                f'<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif></img>')
    elif number >= 10 or number < 0:
        return (f'<h1>Bro it is supposed to be between 0 and 9</h1>'
                f'<a href="/">Get to home</a>')



if __name__ == '__main__':
    app.run(debug=True)
