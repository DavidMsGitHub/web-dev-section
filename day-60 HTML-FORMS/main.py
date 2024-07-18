from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        print(request.form)
        return f"<h1>Username: {request.form['username']} Password: {request.form['password']}</h1>"

if __name__ == '__main__':
    app.run(debug=True)