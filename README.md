### IMAGE APP

```
pyenv virtualenv 3.7.5 imageapi
pyenv local imageapi
pip install -r requirements/dev.txt
export FLASK_APP=app.py
FLASK_DEBUG=1 flask run --no-reload
```

With a little bit more time we could:

- docker-compose
- Implement dataclasses instead of dictionaries.
- Marshalling.
- OpenApi.
- pytests.
- wsgi.
