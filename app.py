import os
import importlib

from logging.config import dictConfig
from flask import Flask, Blueprint
from flask_restful import Api
from flask_restful import Api

from services.agilengine import get_all_images
from endpoints.images.controllers import (
    ImageSearchController,
    ImageController
)
from cache import cache


def create_app():
    app = Flask(__name__)

    config = {
        "production": "ProductionConfig",
        "development": "DevelopmentConfig",
        # "staging": "StagingConfig",
        # "testing": "TestingConfig"
    }

    app = Flask(__name__)

    config_name = os.environ.get('APPLICATION_ENV', 'development')
    config_module = importlib.import_module('config.settings')
    config_class = getattr(config_module, config[config_name])
    app.config.from_object(config_class())
    dictConfig(config_class.LOGGING_CONFIG)


    cache.init_app(app)
    if cache.get('images'): 
        pass
    else:
        images = get_all_images()
        cache.set("images", images)

    images_blueprint = Blueprint('images', __name__)
    app.register_blueprint(images_blueprint)

    api = Api(images_blueprint)

    api.add_resource(ImageSearchController, '/images/<string:search_term>')
    api.add_resource(ImageController, '/images')
    
    return app 

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', use_reloader=True)
