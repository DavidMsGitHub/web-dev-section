from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)


class EditForm(FlaskForm):
    rating = StringField('Your Rating out of 10', render_kw={'style': 'width: 20ch'}, validators=[DataRequired()])
    review = StringField('Your Review', render_kw={'style': 'width: 20ch'}, validators=[DataRequired()])
    submit = SubmitField('Submit Edit')

class AddForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

with app.app_context():
    db.session.commit()

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()

    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = EditForm()
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie= movie, form=form)

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddForm()
    if form.validate_on_submit():
        title_of_movie = form.movie_title.data
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "query": title_of_movie,
        }
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYjc0ZjE2YjU0YjMxNGY1YmQ3OTMwODM0ZjZmYTIwZiIsIm5iZiI6MTcyMTMzMjE3Ni40MjQxODcsInN1YiI6IjY2OTk2ZDcyNzE2MDgyNzJhMDE0M2M2NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.l3y2z7hw1C69Q96BR0-ZIoR40AXl0BIXud-9hwo4XL4"
        }
        response = requests.get(url, params=params, headers=headers)
        movie = response.json()["results"]
        return render_template("select.html", movie=movie)
    return render_template("add.html", form=form)

@app.route("/addingmovie/<id_of_movie>")
def add(id_of_movie):
    url = f"https://api.themoviedb.org/3/movie/{id_of_movie}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYjc0ZjE2YjU0YjMxNGY1YmQ3OTMwODM0ZjZmYTIwZiIsIm5iZiI6MTcyMTMzMjE3Ni40MjQxODcsInN1YiI6IjY2OTk2ZDcyNzE2MDgyNzJhMDE0M2M2NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.l3y2z7hw1C69Q96BR0-ZIoR40AXl0BIXud-9hwo4XL4"
    }
    movie = requests.get(url, headers=headers).json()
    new_movie = Movie(title=movie["original_title"],
                      year=movie["release_date"].split("-")[0],
                      description=movie["overview"],
                      rating=float(movie["vote_average"]),
                      review="No Review Yet",
                      img_url=f"https://image.tmdb.org/t/p/original{movie["poster_path"]}")
    db.session.add(new_movie)
    db.session.commit()
    movie_database_id = Movie.query.filter_by(title=movie["original_title"]).first()
    return redirect(url_for("edit", movie_id=movie_database_id.id))




if __name__ == '__main__':
    app.run(debug=True)
