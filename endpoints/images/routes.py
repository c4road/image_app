
from blueprints.images import (
    images_namespace as images_api
)

from blueprints.images.controllers import (
    ImageController,
)


# Accounts
images_api.add_resource(ImageController, '/')
