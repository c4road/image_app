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
    
    try:
        response = requests.get(
            url,
            headers=headers
        )
        if response.ok:
            return response.json().get('pictures')

    except requests.exceptions.HTTPError:
        logging.exception('HTTP error')
    except requests.exceptions.ConnectionError:
        logging.exception('Connection error')
    except requests.exceptions.Timeout:
        logging.exception('Timeout error')
    except requests.exceptions.RequestException as e:
        logging.exception('Unexpected error')
