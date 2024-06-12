import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Fujitsu/PycharmProjects/Balkanai/balkan_tour/database/balkan_bike_tours.db'
app.config['SECRET_KEY'] = 'your_secret_key'

# Sukuriame katalogą, jei jo nėra
os.makedirs('C:/Users/Fujitsu/PycharmProjects/Balkanai/balkan_tour/database', exist_ok=True)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

from . import routes