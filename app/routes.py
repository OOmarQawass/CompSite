from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from app.models import Part
from app import app


# app = Flask(__name__)

# Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
db_uri = 'sqlite:///' + os.path.join(basedir, "parts.db")
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('home.html', page_title='Home')


@app.route('/how_to')
def how_to():
    return render_template('how_to.html', page_title='HOW TO')


@app.route('/parts_lists')
def part_lists():
    # Query all parts from the database
    parts = Part.query.all()
    return render_template(
        'part_lists.html',
        page_title='Parts List',
        parts=parts
    )


# if __name__ == '__main__':
    # app.run(debug=True)
