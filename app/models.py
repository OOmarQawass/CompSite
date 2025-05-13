from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'C:\dev\CompSite\app\parts.db'  # Path to your database
db = SQLAlchemy(app)

# Define your database model
class Part(db.Model):
    id = db.id(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Route to display data
@app.route('/')
def home():
    parts = Part.query.all()  # Query all parts from the database
    return render_template('Home.html', parts=parts)

if __name__ == '__main__':
    app.run(debug=True)