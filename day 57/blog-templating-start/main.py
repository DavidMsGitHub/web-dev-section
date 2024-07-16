from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/6969388fe85a7eb7b062"
    posts = requests.get(blog_url).json()
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:index>')
def post(index):
    blog_url = "https://api.npoint.io/6969388fe85a7eb7b062"
    posts = requests.get(blog_url).json()
    return render_template("post.html", all_posts=posts, post_number=index)


if __name__ == "__main__":
    app.run(debug=True)
