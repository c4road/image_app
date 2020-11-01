from flask_restful import Resource
from cache import cache
from utils import get_all_images


def get_images_from_cache():
    images = cache.get('images')
    if not images:
        cache.set('images', get_all_images())
    
    return images



class ImageSearchController(Resource):
    """This controller is responsible for accounts operations"""
    def get(self, search_term):
        """Create an account within the XCurrent platform"""
        images = get_images_from_cache()
        search_term = str(search_term).lower().strip()
        response = {
            "image": "No results found"
        }
        search_results = []
        for image in images:
            print(image)
            id_ = image.get('id', '')
            author = image.get('author', '').lower()
            camera = image.get('camera', '').lower()
            tags = image.get("tags", '').lower()

            if (search_term == id_) or \
                (search_term == author) or \
                (search_term in camera) or \
                (search_term in tags):
                search_results.append(image)

        response.update({"results": search_results})
        return response


class ImageController(Resource):

    def get(self):
        """Create an account within the XCurrent platform"""
        images = get_images_from_cache()
        response = {
            'images': images
        }
        return response
