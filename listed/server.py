import sys
from gevent.pywsgi import WSGIServer
from listed.app import app
from listed.config import PORT


server = WSGIServer(('', PORT), app)


def dev():
    app.run('0.0.0.0', port=PORT, debug=True)

def prod():
    server.serve_forever()


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'dev':
        dev()
    else:
        prod()
