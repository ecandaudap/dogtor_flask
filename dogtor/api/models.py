from dogtor.db import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship


class User(db.Model):
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String, unique=True, nullable=False)
    email = mapped_column(String, unique=True)

class Owner(db.Model):
    id = mapped_column(Integer, primary_key=True)
    ownername = mapped_column(String, unique=True, nullable=False)
    email = mapped_column(String, unique=True)
    pets = db.relationship('Pet', backref='owner')

class Pet(db.Model):
    id = mapped_column(Integer, primary_key=True)
    petname = mapped_column(String, unique=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    species = db.relationship('Pet', backref='species')

class Species(db.Model):
    id = mapped_column(Integer, primary_key=True)
    speciename = mapped_column(String, unique=True, nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))



