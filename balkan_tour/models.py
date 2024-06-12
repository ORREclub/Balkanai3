from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from . import db, bcrypt

class Tour(db.Model):
    __tablename__ = 'tours'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    location = Column(String)
    bookings = relationship('Booking', back_populates='tour')
    clients = relationship('Client', back_populates='tour')
    date_start = Column(DateTime)  # Pradžios data
    date_end = Column(DateTime)  # Pabaigos data

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    bookings = relationship('Booking', back_populates='user')

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class Bike(db.Model):
    __tablename__ = 'bikes'

    id = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(String)
    type = Column(String)
    bookings = relationship('Booking', back_populates='bike')

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    bike_id = Column(Integer, ForeignKey('bikes.id'))
    tour_id = Column(Integer, ForeignKey('tours.id'))
    date = Column(DateTime)

    user = relationship('User', back_populates='bookings')
    bike = relationship('Bike', back_populates='bookings')
    tour = relationship('Tour', back_populates='bookings')

class Client(db.Model):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    tour_id = Column(Integer, ForeignKey('tours.id'))
    tour_name = Column(String)

    tour = relationship('Tour', back_populates='clients')