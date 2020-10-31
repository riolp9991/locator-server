#pylint: disable=E0401
from app import app, db
from flask import jsonify, request, Response
from schemas.items_schema import Item, item_schema, items_schema

PREFIX = '/api/items/'


@app.route(PREFIX, methods=['GET', 'POST'])
def get_and_create_items():
    try:
        if request.method == 'GET':
            all_items = Item.query.all()
            return jsonify(items_schema.dump(all_items))

        if request.method == 'POST':
            data = request.json
            name = data['name']
            description = data['description']
            location = data['location']

            new_item = Item(name, description, location)

            db.session.add(new_item)
            db.session.commit()

            return item_schema.jsonify(new_item)
    except:
        return Response('Algo ha salido mal')
