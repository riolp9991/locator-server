#pylint: disable=E0401
from app import app
from models.location_model import Location
from flask import jsonify, request

PREFIX = '/api/locations'

@app.route(PREFIX + '/', methods=['GET'])
def index():
    return jsonify({'TODO:': 'GET ALL LOCATIONS'})
