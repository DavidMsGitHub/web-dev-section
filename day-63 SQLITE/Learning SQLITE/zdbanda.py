#
# import sqlite3
#
# db = sqlite3.connect('books-data.db')
# cursor = db.cursor()
#
# cursor.execute("INSERT INTO books VALUES(2, 'Harry Pottera', 'J. K. Rowling', '9.3')")
# db.commit()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title, self.author, self.rating}>'


with app.app_context():
    all_books = db.session.query(Book).all()
    print(all_books)

# print(admin)