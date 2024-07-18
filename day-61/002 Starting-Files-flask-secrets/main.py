from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'Dato2006mix23!Dix'
Bootstrap(app)


class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(granular_message=True)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=32,
                                                                            message=f"Please enter atleast %(min)d characters")])
    submit = SubmitField('Login')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

@app.route("/success")
def success():
    return '<h1 style="color: green;">SUCCESS</h1>'



if __name__ == '__main__':
    app.run(debug=True)