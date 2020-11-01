from flask_restful import Resource



class ImageController(Resource):
    """This controller is responsible for accounts operations"""

    def get(self):
        """Create an account within the XCurrent platform"""
        endpoint = "/config/accounts"

        return {"hola": "mundo"}
    

class ImageSearchController(Resource):
    pass