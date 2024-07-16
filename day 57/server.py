from flask import Flask, render_template
import requests
from datetime import datetime
app = Flask(__name__)

name = "Michael"
def get_gender():
    respond = requests.get("https://api.genderize.io", params={"name": name}).text
    print(respond)


get_gender()
year_now = datetime.now().year
@app.route('/<name>')
def hello(name):
    genderize = requests.get("https://api.genderize.io", params={"name": name}).json()
    gender = genderize["gender"]
    agify = requests.get("https://api.agify.io", params={"name": name}).json()
    age = agify["age"]
    return render_template("index.html", age=age, name=name.title(), gender=gender, year_now=year_now)


@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/d2d14b35c0765ea30e3a"
    posts = requests.get(blog_url).json()
    return render_template("blog.html", posts=posts)


if __name__ == '__main__':
    app.run(debug=True)