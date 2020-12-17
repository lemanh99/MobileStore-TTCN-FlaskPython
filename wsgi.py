import os
from shop import app as _application

def application(environ, start_response):
    os.environ['ENVTYPE'] = environ['ENVTYPE']
    return _application(environ, start_response)

if __name__ == '__main__':
    _application.run(debug=True, threaded=True)
