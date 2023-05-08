#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id==id).first()
    response_body = f''
    response_body += f'<ul><h2>ID: {animal.id}</h2></ul>'
    response_body += f'<ul><h2>Name: {animal.name}</h2></ul>'
    response_body += f'<ul><h2>Species: {animal.species}</h2></ul>'
    response_body += f'<ul><h2>Zookeeper: {animal.zookeeper}</h2></ul>'
    response_body += f'<ul><h2>Enclosure: {animal.enclosure}</h2></ul>'
    
    return make_response(response_body,200)

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Animal.id==id).first()
    response_body = f''
    response_body += f'<ul><h2>ID: {zookeeper.id}</h2></ul>'
    response_body += f'<ul><h2>Name: {zookeeper.name}</h2></ul>'
    response_body += f'<ul><h2>Species: {zookeeper.birthday}</h2></ul>'
    for animal in zookeeper.animals:
        response_body += f'<ul><h2>Animal: {animal.name}</h2></ul>'

    return make_response(response_body,200)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id==id).first()
    response_body = f''
    response_body += f'<ul><h2>ID: {enclosure.id}</h2></ul>'
    response_body += f'<ul><h2>Environment: {enclosure.environment}</h2></ul>'
    response_body += f'<ul><h2>Open to Visitors: {enclosure.open_to_visitors}</h2></ul>'
    for animal in enclosure.animals:
        response_body += f'<ul><h2>Animal: {animal.name}</h2></ul>'

    return make_response(response_body,200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
