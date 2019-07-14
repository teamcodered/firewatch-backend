# from app import flask_app, db

def setupApp(flask_app, db):
    
    from app.api.models import Sensor, Drone

    from app.api.controllers import sensor_api_blueprint, drone_api_blueprint

    flask_app.register_blueprint(sensor_api_blueprint)
    flask_app.register_blueprint(drone_api_blueprint)

    db.create_all()


