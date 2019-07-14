from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

from app.api import setupApp

flask_app = Flask(__name__)

flask_app.config.from_object('config')
db = SQLAlchemy(flask_app)
manager = APIManager(flask_app)
setupApp(flask_app, db)



# mod_api = Blueprint('api', __name__, url_prefix='/api')