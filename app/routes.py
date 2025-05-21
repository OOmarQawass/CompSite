from app import app
from flask import render_template, abort
from flask_sqlalchemy import SQLAlchemy  # no more boring old SQL for us!
import os


basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "parts.db")
db.init_app(app)
      

import app.models as models


# basic route
@app.route('/')
def root():
    return render_template('home.html', page_title='HOME')


# about route
@app.route('/How-to')  # note the leading slash, it’s important
def about():
    return render_template('How-to.html', page_title='HOW-TO') 


@app.route('/all_parts')
def all_parts():
  all_parts = models.Part.query.all()
  return render_template("Part Lists.html", parts=parts)


# Now lets display one pizza using SQLAlchemy
@app.route('/pizza/<int:id>')
def parts(id):
    # get the pizza, but throw a 404 if the id doesn't exist
    parts = models.Part.query.filter_by(id=id).first_or_404()
    print(parts, models)  # DEBUG
    # title = pizza[1].upper() + ' PIZZA' # see Pizza class __repr__
    return render_template('Part Lists.html', parts=parts)


@app.route('/base/<int:id>')
def base(id):
    pizzas = models.Pizza.query.filter_by(base=id).all()
    return render_template("pizzas.html", pizzas=pizzas)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

#if __name__ == "__main__":
#    app.run(debug=True)