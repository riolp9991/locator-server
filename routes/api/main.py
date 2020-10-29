# pylint: disable=E0401
from app import app
from flask import jsonify, request
from models.location_model import Location


@app.route('/api/', methods=['GET'])
def get():
    print("Hello Console")
    return jsonify({'msg':"Hello World"})


@app.route('/api/test/<name>', methods=['GET'])
def getTest(name):
    return jsonify({'msg': f"Welcome {name}"})


prueba = Location("Mario")
