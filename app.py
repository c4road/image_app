from flask import Flask, Blueprint
from flask_restful import Api
from utils import get_all_images
from endpoints.images.controllers import (
    ImageSearchController,
    ImageController
)
from flask_restful import Api
from cache import cache



def create_app():
    app = Flask(__name__)
    cache.init_app(app)
    if cache.get('images'): 
        pass
    else:
        images = get_all_images()
        cache.set("images", images)
    images_blueprint = Blueprint('images', __name__)
    api = Api(images_blueprint)

    api.add_resource(ImageSearchController, '/images/<string:search_term>')
    api.add_resource(ImageController, '/images')
    app.register_blueprint(images_blueprint)

    return app 

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', use_reloader=True)
