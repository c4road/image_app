import os


class Config(object):

    CACHE_DEFAULT_TIMEOUT = os.environ.get('CACHE_DEFAULT_TIMEOUT')
    LOGGING_CONFIG = {
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level':  os.environ.get('LOG_LEVEL', 'INFO'),
            'handlers': ['wsgi']
        }
    }


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass
