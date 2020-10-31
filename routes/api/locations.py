#pylint: disable=E0401
from app import app, db
from flask import jsonify, request, Response
from schemas.location_schema import Location, location_schema, locations_schema 

PREFIX = '/api/locations/'


@app.route(PREFIX, methods=['GET', 'POST'])
def get_and_create_location():
    try:
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
    except:
        return Response('Something Went Wrong', status=500)
        

@app.route(PREFIX + '<id>', methods=['GET', 'PUT', 'DELETE'])
def locations_get_one_update_delete(id):
    try:
        current_location = Location.query.get(id)
        if current_location == None:
            return Response("The Location Was Not Found", status=400)

        if request.method == 'GET':
            return location_schema.jsonify(current_location)

        if request.method == 'PUT':
            data = request.json

            name = data['name']
            parent = data['parent']
            description = data['parent']

            current_location.name = name
            current_location.parent_id = parent
            current_location.description = description

            db.session.commit()

            return location_schema.jsonify(current_location)

        if request.method == 'DELETE':
            db.session.delete(current_location)
            db.session.commit()

            return location_schema.jsonify(current_location)

    except:
        return Response('Something Went Worng', status=500)


@app.route(PREFIX + '<id>/childs', methods=['GET'])
def get_location_childs(id):
    try:
        father_location = Location.query.get(id)
        result = locations_schema.dump(father_location.child)
        return jsonify(result)
    except:
        return Response("Something Went Wrong", status=500)

@app.route(PREFIX + '<id>/breadcrumb', methods=['GET'])
def get_location_nodes(id):
    try:
        current_location = Location.query.get(id)
        
        if current_location == None:
            return Response("The location does not exist", status=400)

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

        node_list = node_list.reverse()
        return jsonify(result = node_list)
    except:
        return Response("No se pudo generar la lista", status=500)
