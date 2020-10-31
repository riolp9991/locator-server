from app import db, ma


class Location(db.Model):
    __tablename__ = "locations"
    #pylint: disable=E1101
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200))
    parent_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

    child = db.relationship('Location', cascade='all,delete', backref=db.backref('parent', remote_side=[id]))
    
    def __init__(self, name, description, parent_id = None):
        self.name = name
        self.description = description
        self.parent_id = parent_id


class LocationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'parent_id')




location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)
