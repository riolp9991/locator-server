#pylint: disable=E0401
from app import app, db
from flask import jsonify, request, Response
from schemas.location_schema import Location, location_schema, locations_schema 

PREFIX = '/api/locations/'


@app.route(PREFIX, methods=['GET', 'POST'])
def get_and_create_location():
    if request.method == 'GET':
        all_locations = Location.query.all()
        result = locations_schema.dump(all_locations)
        print(result)
        return jsonify(result)

    if request.method == 'POST':
        print ("REQUEST",request.json)
        name = request.json['name']
        descr = request.json['description']
        parent = request.json['parent'] if 'parent' in request.json else None
    
        new_location = Location(name, descr, parent)

        db.session.add(new_location)
        db.session.commit()

        return location_schema.jsonify(new_location)
        

@app.route(PREFIX + '<id>', methods=['GET', 'PUT', 'DELETE'])
def locations_get_one_update_delete(id):
    current_location = Location.query.get(id)
    if request.method == 'GET':
        return location_schema.jsonify(current_location)


    if request.method == 'PUT':
        return jsonify({'TODO': 'UPDATE A LOCATION'})

    if request.method == 'DELETE':
        return jsonify({'TODO': 'DELETE A LOCATION'})


@app.route(PREFIX + '<id>/childs', methods=['GET'])
def get_location_childs(id):
    father_location = Location.query.get(id)

    childs = father_location.child

    result = locations_schema.dump(childs)
    return jsonify(result)

@app.route(PREFIX + '<id>/breadcrum', methods=['GET'])
def get_location_nodes(id):
    current_location = Location.query.get(id)
    

    node_list = []
    node_list.append({
        'id': current_location.id,
        'name': current_location.name,
        'descriptioni': current_location.description,
        'parent': current_location.parent_id
        })

    while not current_location.parent == None:
        current_location = current_location.parent
        node_list.append({
            'id': current_location.id,
            'name': current_location.name,
            'descriptioni': current_location.description,
            'parent': current_location.parent_id
            })

    return jsonify(result = node_list)
