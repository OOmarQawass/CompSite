from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from app import app
from app.models import cpu, gpu, ram, cooler, psu, storage, case, motherboard


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
    parts = {
            "cpu": cpu.query.all(),
            "gpu": gpu.query.all(),
            "ram": ram.query.all(),
            "cooler": cooler.query.all(),
            "psu": psu.query.all(),
            "storage": storage.query.all(),
            "case": case.query.all(),
            "motherboard": motherboard.query.all()
}

# if __name__ == '__main__':
    # app.run(debug=True)
