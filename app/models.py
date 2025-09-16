from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class cpu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    socket = db.Column(db.String(50), nullable=False)
    motherboards = db.relationship('motherboard', backref='cpu', lazy=True)


class ram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.String(50), nullable=False)
    speed = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    ram_motherboard_compatibilities = db.relationship(
        'ram_motherboard_compatibility', backref='motherboard', lazy=True)


class cooler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    motherboards = db.relationship('motherboard', backref='cooler', lazy=True)


class case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    form_factor = db.Column(db.String(50), nullable=False)
    motherboards = db.relationship('motherboard', backref='case', lazy=True)


class gpu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    vram = db.Column(db.String(50), nullable=False)


class psu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    wattage = db.Column(db.String(50), nullable=False)
    effeciency_rating = db.Column(db.String(50), nullable=False)


class storage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)


class motherboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    chipset = db.Column(db.String(50), nullable=False)
    form_factor = db.Column(db.String(50), nullable=False)
    cpu_id = db.Column(db.Integer, db.ForeignKey('cpu.id'), nullable=False)
    cooler_id = db.Column(db.Integer, db.ForeignKey('cooler.id'), nullable=False)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    ram_motherboard_compatibilities = db.relationship('ram_motherboard_compatibility', lazy=True)


class ram_motherboard_compatibility(db.Model):
    ram_id = db.Column(db.Integer, db.ForeignKey('ram.id'), primary_key=True)
    motherboard_id = db.Column(db.Integer, db.ForeignKey('motherboard.id'), primary_key=True)
