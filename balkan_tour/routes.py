# routes.py
from datetime import datetime
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from . import app, db, bcrypt
from .models import User, Tour, Booking, Client
from .forms import LoginForm, RegistrationForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/tours')
def tours():
    return render_template('tours.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/mtb_east_rodopai')
def mtb_east_rodopai():
    return render_template('mtb_east_rodopai.html')

@app.route('/mtb_rila_rodopai')
def mtb_rila_rodopai():
    return render_template('mtb_rila_rodopai.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Čia įvykdoma registracijos logika
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')

from flask_login import login_required

@app.route('/add_tour', methods=['GET', 'POST'])
@login_required  # Šis maršrutas pasiekiamas tik prisijungusiems vartotojams
def add_tour():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']
        date_start = datetime.strptime(request.form['date_start'], '%Y-%m-%d')
        date_end = datetime.strptime(request.form['date_end'], '%Y-%m-%d')

        new_tour = Tour(name=name, location=location, description=description,
                        date_start=date_start, date_end=date_end)
        db.session.add(new_tour)
        db.session.commit()

        return redirect(url_for('add_tour'))  # Peradresuoti į tą patį maršrutą po naujo turo pridėjimo

    else:  # GET užklausa
        tours = Tour.query.all()
        return render_template('add_tour.html', tours=tours)



@app.route('/clients', methods=['GET', 'POST'])
@login_required
def clients():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        tour_id = request.form['tour']

        # Gauname turą iš duomenų bazės
        tour = Tour.query.get(tour_id)
        tour_name = tour.name if tour else None

        # Sukuriame naują kliento įrašą su turu
        new_client = Client(name=name, surname=surname, email=email, tour_id=tour_id, tour_name=tour_name)

        # Įtraukiame naują klientą į duomenų bazę
        db.session.add(new_client)
        db.session.commit()

        return redirect(url_for('clients'))

    # Gauti visus klientus ir turus iš duomenų bazės
    clients = Client.query.all()
    tours = Tour.query.all()
    return render_template('clients.html', clients=clients, tours=tours)

@app.route('/tour_details/<int:tour_id>')
@login_required
def tour_details(tour_id):
    tour = Tour.query.get(tour_id)
    clients = Client.query.filter_by(tour_id=tour_id).all()
    return render_template('tour_details.html', tour=tour, clients=clients)

@app.route('/delete_tour/<int:tour_id>', methods=['POST'])
def delete_tour(tour_id):
    tour = Tour.query.get(tour_id)
    db.session.delete(tour)
    db.session.commit()
    flash('Tour deleted successfully!', 'success')
    return redirect(url_for('add_tour'))

@app.route('/delete_client/<int:client_id>', methods=['POST'])
def delete_client(client_id):
    client = Client.query.get(client_id)
    db.session.delete(client)
    db.session.commit()
    flash('Client deleted successfully!', 'success')
    return redirect(url_for('clients'))

@app.route('/calendar')
def calendar():
    tours = Tour.query.all()  # Gauti visus turus iš duomenų bazės
    return render_template('calendar.html', tours=tours)

if __name__ == "__main__":
    app.run(debug=True)
