from flask import Flask, render_template,request
from requests import get
import smtplib


my_email = "dato2006213@gmail.com"
password = "tbzs fdii uarh ajhh"


about_bg = "about-bg.jpg"
contact_bg = "contact-bg.jpeg"
home_bg = "home-bg.jpg"
post_bg = "post-bg.jpg"

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Secure the connection
        server.login(my_email, password)
        server.sendmail(from_addr=email, to_addrs=email, msg=email_message)

app = Flask(__name__)
@app.route("/")
def home():
    articles = get("https://api.npoint.io/b44e965047e1c4964809").json()
    return render_template("index.html", bg=home_bg, articles=articles)

@app.route("/about")
def about():
    return render_template("about.html", bg=about_bg)

@app.route("/contact", methods=["POST","GET"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", bg=contact_bg, sent=True)
    else:
        return render_template("contact.html", bg=contact_bg, sent=False)



@app.route("/post/<int:id>")
def post(id):
    articles = get("https://api.npoint.io/b44e965047e1c4964809").json()
    return render_template("post.html", bg=post_bg, article=articles[id-1])


if __name__ == "__main__":
    app.run(debug=True)


