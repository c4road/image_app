from flask import Flask, Blueprint
from flask_restful import Api
from utils import get_all_images
from endpoints.images.controllers import ImageController
from flask_restful import Api
from flask_caching import Cache

cache = Cache(config={
    "DEBUG": True,
    "CACHE_TYPE": "simple", 
    "CACHE_DEFAULT_TIMEOUT": 300
})

app = Flask(__name__)
cache.init_app(app)
images_blueprint = Blueprint('images', __name__)
api = Api(images_blueprint)


api.add_resource(ImageController, '/images')
app.register_blueprint(images_blueprint)



if __name__ == '__main__':
    images = get_all_images()
    cache.set("images", images)
    app.run(debug=True, host='0.0.0.0')
