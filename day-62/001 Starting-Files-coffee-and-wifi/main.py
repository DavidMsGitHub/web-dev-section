from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, SelectField
from wtforms.fields.datetime import TimeField
from wtforms.validators import DataRequired, URL, Email, EqualTo, ValidationError
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location in URL', validators=[DataRequired(), URL(message='Must be a valid URL')])
    open_time = TimeField('Open time in HH:mm', validators=[DataRequired()])
    close_time = TimeField('Close time in HH:mm', validators=[DataRequired()])
    coffee_rate = SelectField(choices=[('☕️', '☕️'), ('☕️☕️', '☕️☕️'),('☕️☕️☕️', '☕️☕️☕️'), ('☕️☕️☕️☕️', '☕️☕️☕️☕️'), ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')])
    wifi_rate = SelectField(choices=[('☕️', '☕️'), ('☕️☕️', '☕️☕️'),('☕️☕️☕️', '☕️☕️☕️'), ('☕️☕️☕️☕️', '☕️☕️☕️☕️'), ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')])
    power_outlet = SelectField(choices=[('☕️', '☕️'), ('☕️☕️', '☕️☕️'),('☕️☕️☕️', '☕️☕️☕️'), ('☕️☕️☕️☕️', '☕️☕️☕️☕️'), ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    form.validate_on_submit()
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv", "a") as file:
            file.write(f"\n{form.cafe.data},{form.location.data},{form.open_time.data},{form.close_time.data},{form.coffee_rate.data},{form.wifi_rate.data},{form.power_outlet.data}")

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
