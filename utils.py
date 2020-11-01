import json
import logging
import requests

from functools import wraps
from flask_restful import abort


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """
        """

        agile_auth = "http://interview.agileengine.com/auth"
        status_code = 500
        payload = {"apiKey": "23567b218376f79d9415"}
        access_token = None
        headers = {'content-type': 'application/json'}
        try:
            response = requests.post(
                agile_auth,
                data=json.dumps(payload),
                headers=headers
            )
            if response.ok:

                access_token = response.json().get(
                    'token',
                    None
                )

        except requests.exceptions.HTTPError:
            logging.exception('HTTP error')
        except requests.exceptions.ConnectionError:
            logging.exception('Connection error')
        except requests.exceptions.Timeout:
            logging.exception('Timeout error')
        except requests.exceptions.RequestException:
            logging.exception('Unexpected error')
        except Exception:
            logging.exception('Generic exception error')
        else:
            status_code = response.status_code

        if access_token:
            return f(*args, access_token=access_token, **kwargs)
        else:
            abort(status_code)
    return decorated_function


@token_required
def get_all_images(access_token):
    """This function is used to send http requests to Xcurrent
    """
    url = 'http://interview.agileengine.com/images'
    headers = {
            'Authorization': 'Bearer ' + access_token
        }
    images = []
    try:
        logging.info("Fetching all the images")
        response = requests.get(
            url,
            headers=headers
        )
        if response.ok:
            total_pages = response.json().get('pageCount')
            images = response.json().get('pictures')
            for i in range(2,total_pages):
                paginated_url = f'http://interview.agileengine.com/images?page={i}'
                response = requests.get(
                    paginated_url,
                    headers=headers
                )
                images += response.json().get('pictures')
                print(f"fetched {i} of {total_pages}")
        
        detailed_images = []
        for image in images:
            detail_url = f"http://interview.agileengine.com/images/{image.get('id')}"
            
            print(f"Retrieving detail of {image['id']}")
            response = requests.get(
                detail_url,
                headers=headers
            )
            if response.ok:
                detailed_images.append(response.json())
        return detailed_images
    except requests.exceptions.HTTPError:
        logging.exception('HTTP error')
    except requests.exceptions.ConnectionError:
        logging.exception('Connection error')
    except requests.exceptions.Timeout:
        logging.exception('Timeout error')
    except requests.exceptions.RequestException as e:
        logging.exception('Unexpected error')
