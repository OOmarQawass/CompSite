from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models import cpu, ram, cooler, case, gpu, psu, storage, motherboard
from app.models import User
from flask_login import login_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_login import logout_user

# Forms for login and adding parts
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class CPUForm(FlaskForm):
    model = StringField('Model', validators=[DataRequired()])
    socket = StringField('Socket', validators=[DataRequired()])
    submit = SubmitField('Add CPU')


class GPUForm(FlaskForm):
    model = StringField('Model', validators=[DataRequired()])
    vram = StringField('VRAM', validators=[DataRequired()])
    submit = SubmitField('Add GPU')


class CoolerForm(FlaskForm):
    model = StringField('Model', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    size = StringField('Size', validators=[DataRequired()])
    submit = SubmitField('Add Cooler')


class MotherboardForm(FlaskForm):
    model = StringField('Model', validators=[DataRequired()])
    socket = StringField('Socket', validators=[DataRequired()])
    submit = SubmitField('Add Motherboard')


class RAMForm(FlaskForm):
    model = StringField('Model', validators=[DataRequired()])
    capacity = StringField('Capacity', validators=[DataRequired()])
    speed = StringField('Speed', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    submit = SubmitField('Add RAM')


class PSUForm(FlaskForm):
    model = StringField('Model', validators=[DataRequired()])
    wattage = StringField('Wattage', validators=[DataRequired()])
    submit = SubmitField('Add PSU')


class CaseForm(FlaskForm):
    model = StringField('Model', validators=[DataRequired()])
    submit = SubmitField('Add Case')


class StorageForm(FlaskForm):
    model = StringField('Model', validators=[DataRequired()])
    capacity = StringField('Capacity', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    submit = SubmitField('Add Storage')

#App routes
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('admin'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)


@app.route('/')
def home():
    return render_template('home.html', page_title='Home')


@app.route('/how_to')
def how_to():
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


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    cpu_form = CPUForm()
    gpu_form = GPUForm()
    cooler_form = CoolerForm()
    motherboard_form = MotherboardForm()
    ram_form = RAMForm()
    psu_form = PSUForm()
    case_form = CaseForm()
    storage_form = StorageForm()

    cpus = cpu.query.all()
    gpus = gpu.query.all()
    coolers = cooler.query.all()
    motherboards = motherboard.query.all()
    rams = ram.query.all()
    psus = psu.query.all()
    cases = case.query.all()
    storages = storage.query.all()

    # CPU
    if cpu_form.submit.data and cpu_form.validate_on_submit():
        new_cpu = cpu(model=cpu_form.model.data, socket=cpu_form.socket.data)
        db.session.add(new_cpu)
        db.session.commit()
        flash('CPU added!')
        return redirect(url_for('admin'))

    # GPU
    if gpu_form.submit.data and gpu_form.validate_on_submit():
        new_gpu = gpu(model=gpu_form.model.data)
        db.session.add(new_gpu)
        db.session.commit()
        flash('GPU added!')
        return redirect(url_for('admin'))

    # Cooler
    if cooler_form.submit.data and cooler_form.validate_on_submit():
        new_cooler = cooler(model=cooler_form.model.data, type=cooler_form.type.data, size=cooler_form.size.data)
        db.session.add(new_cooler)
        db.session.commit()
        flash('Cooler added!')
        return redirect(url_for('admin'))

    # Motherboard
    if motherboard_form.submit.data and motherboard_form.validate_on_submit():
        new_motherboard = motherboard(model=motherboard_form.model.data, socket=motherboard_form.socket.data)
        db.session.add(new_motherboard)
        db.session.commit()
        flash('Motherboard added!')
        return redirect(url_for('admin'))

    # RAM
    if ram_form.submit.data and ram_form.validate_on_submit():
        new_ram = ram(model=ram_form.model.data, capacity=ram_form.capacity.data, speed=ram_form.speed.data, type=ram_form.type.data)
        db.session.add(new_ram)
        db.session.commit()
        flash('RAM added!')
        return redirect(url_for('admin'))

    # PSU
    if psu_form.submit.data and psu_form.validate_on_submit():
        new_psu = psu(model=psu_form.model.data, wattage=psu_form.wattage.data)
        db.session.add(new_psu)
        db.session.commit()
        flash('PSU added!')
        return redirect(url_for('admin'))

    # Case
    if case_form.submit.data and case_form.validate_on_submit():
        new_case = case(model=case_form.model.data)
        db.session.add(new_case)
        db.session.commit()
        flash('Case added!')
        return redirect(url_for('admin'))

    # Storage
    if storage_form.submit.data and storage_form.validate_on_submit():
        new_storage = storage(model=storage_form.model.data, capacity=storage_form.capacity.data, type=storage_form.type.data)
        db.session.add(new_storage)
        db.session.commit()
        flash('Storage added!')
        return redirect(url_for('admin'))

    return render_template(
        'admin.html',
        cpu_form=cpu_form,
        gpu_form=gpu_form,
        cooler_form=cooler_form,
        motherboard_form=motherboard_form,
        ram_form=ram_form,
        psu_form=psu_form,
        case_form=case_form,
        storage_form=storage_form,
        cpus=cpus,
        gpus=gpus,
        coolers=coolers,
        motherboards=motherboards,
        rams=rams,
        psus=psus,
        cases=cases,
        storages=storages
    )

# Delete routes for each part


@app.route('/delete_cpu/<int:id>')
@login_required
def delete_cpu(id):
    item = cpu.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('CPU deleted!')
    return redirect(url_for('admin'))


@app.route('/delete_gpu/<int:id>')
@login_required
def delete_gpu(id):
    item = gpu.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('GPU deleted!')
    return redirect(url_for('admin'))


@app.route('/delete_cooler/<int:id>')
@login_required
def delete_cooler(id):
    item = cooler.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Cooler deleted!')
    return redirect(url_for('admin'))


@app.route('/delete_motherboard/<int:id>')
@login_required
def delete_motherboard(id):
    item = motherboard.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Motherboard deleted!')
    return redirect(url_for('admin'))


@app.route('/delete_ram/<int:id>')
@login_required
def delete_ram(id):
    item = ram.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('RAM deleted!')
    return redirect(url_for('admin'))


@app.route('/delete_psu/<int:id>')
@login_required
def delete_psu(id):
    item = psu.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('PSU deleted!')
    return redirect(url_for('admin'))


@app.route('/delete_case/<int:id>')
@login_required
def delete_case(id):
    item = case.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Case deleted!')
    return redirect(url_for('admin'))


@app.route('/delete_storage/<int:id>')
@login_required
def delete_storage(id):
    item = storage.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Storage deleted!')
    return
