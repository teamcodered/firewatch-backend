from app import db

class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime, default = db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default = db.func.current_timestamp())


class Device(Base):
    __abstract__ = True

    description = db.Column(db.String(250), nullable = True)

class Sensor(Device):

    __tablename__ = 'Sensor'

    lon = db.Column(db.Float)
    lat = db.Column(db.Float)

class Drone(Device):

    __tablename__ = 'Drone'