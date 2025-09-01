from flask import Flask, jsonify, render_template
from app import app, db
from app.models import cpu, ram, cooler, case, gpu, psu, storage, motherboard


# Create tables if they don't exist
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # Renders the home page.
    return render_template('home.html', page_title='Home')


@app.route('/how_to')
def how_to():
    # Renders the how-to page.
    return render_template('how_to.html', page_title='HOW TO')


@app.route('/parts_lists')
def parts_lists():
    cpus = cpu.query.all()
    rams = ram.query.all()
    coolers = cooler.query.all()
    cases = case.query.all()
    gpus = gpu.query.all()
    psus = psu.query.all()
    storages = storage.query.all()
    motherboards = motherboard.query.all()
    return render_template(
        'parts_lists.html',
        page_title='Parts Lists',
        cpus=cpus,
        rams=rams,
        coolers=coolers,
        cases=cases,
        gpus=gpus,
        psus=psus,
        storages=storages,
        motherboards=motherboards
    )
