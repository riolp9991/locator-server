# pylint: disable=E0401
from app import app
from flask import jsonify, request


@app.route('/api/', methods=['GET'])
def get():
    print("Hello Console")
    return jsonify({'msg':"Hello World"})


@app.route('/api/test/<name>', methods=['GET'])
def getTest(name):
    return jsonify({'msg': f"Welcome {name}"})
