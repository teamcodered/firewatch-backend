from app import flask_app, manager

from app.api.models import Drone, Sensor

sensor_api_blueprint = manager.create_api_blueprint(Sensor, methods = ['GET', 'POST', 'DELETE', 'PATCH'])
drone_api_blueprint = manager.create_api_blueprint(Drone, methods = ['GET', 'POST', 'DELETE', 'PATCH'])
