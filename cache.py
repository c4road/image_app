from flask_caching import Cache

cache = Cache(config={
    "DEBUG": True,
    "CACHE_TYPE": "simple", 
    "CACHE_DEFAULT_TIMEOUT": 3000
})
