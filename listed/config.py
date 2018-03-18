import os

VERSION = 'v0.0.5'

STORAGE = os.environ.get('LISTED_STORAGE', '~/.listed')
PORT = int(os.environ.get('LISTED_PORT', 8080))
