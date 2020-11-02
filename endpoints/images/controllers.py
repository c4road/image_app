from flask_restful import Resource

from services.agilengine import get_all_images
from cache import cache



def get_images_from_cache():
    images = cache.get('images')
    if not images:
        cache.set('images', get_all_images())
    
    return images

def filter_images(images, search_term):
    search_results = []
    for image in images:
        id_ = image.get('id', '')
        author = image.get('author', '').lower()
        camera = image.get('camera', '').lower()
        tags = image.get("tags", '').lower()

        if (search_term == id_):
            return {"results": [image] } 

        elif (search_term == author) or \
             (search_term in camera) or \
             (search_term in tags):

            results = search_results.append(image)

    return {"results": search_results} 


class ImageSearchController(Resource):
    """This controller is responsible for accounts operations"""
    def get(self, search_term):
        """Create an account within the XCurrent platform"""
        images = get_images_from_cache()
        search_term = str(search_term).lower().strip()
        response = filter_images(images, search_term)

        return response, 200


class ImageController(Resource):

    def get(self):
        """Create an account within the XCurrent platform"""
        images = get_images_from_cache()
        response = {
            'images': images
        }
        return response, 200 
