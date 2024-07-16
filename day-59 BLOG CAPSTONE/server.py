from flask import Flask, render_template
from requests import get


about_bg = "about-bg.jpg"
contact_bg = "contact-bg.jpeg"
home_bg = "home-bg.jpg"
post_bg = "post-bg.jpg"

app = Flask(__name__)
@app.route("/")
def home():
    articles = get("https://api.npoint.io/b44e965047e1c4964809").json()
    return render_template("index.html", bg=home_bg, articles=articles)

@app.route("/about")
def about():
    return render_template("about.html", bg=about_bg)

@app.route("/contact")
def contact():
    return render_template("contact.html", bg=contact_bg)

@app.route("/post/<int:id>")
def post(id):
    articles = get("https://api.npoint.io/b44e965047e1c4964809").json()
    return render_template("post.html", bg=post_bg, article=articles[id-1])


if __name__ == "__main__":
    app.run(debug=True)