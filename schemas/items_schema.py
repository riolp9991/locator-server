from app import  ma, db


class Item(db.Model):
    __tablename__ = 'items'
    #pylint: disable="E1101
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id', nullable=False))


    def __init__(self,name,description,location_id=None):
        self.name = name
        self.description = description
        self.location_id = location_id


class ItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'location_id')



item_schema = ItemSchema()
idems_schema = ItemSchema(many=True)
