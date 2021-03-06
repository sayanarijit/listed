# Listed

List and display files in the web

[![PyPI version](https://img.shields.io/pypi/v/listed.svg)](https://pypi.org/p/listed)
[![Build Status](https://travis-ci.org/sayanarijit/listed.svg?branch=master)](https://travis-ci.org/sayanarijit/listed)


### Installation

```
# Setup virtual environment
pip install --user virtualenv
python -m virtualenv ~/.venv
source ~/.venv/bin/activate

# Install via pip
pip install -U listed
```


### Configuration

| Config       | Environment variable | Default     |
| ------------ | -------------------- | ----------- |
| File storage | LISTED_STORAGE       | '~/.listed' |


### Run

```
# Add some demo files
mkdir ~/.listed
wget https://raw.githubusercontent.com/sayanarijit/listed/master/demofiles/a.md -O ~/.listed/a.md
wget https://raw.githubusercontent.com/sayanarijit/listed/master/demofiles/b.txt -O ~/.listed/b.txt

# Run production instance  (robust WSGI server)
gunicorn -b 0.0.0.0:8080 listed.app:app

# Or run development instance (for debugging only)
FLASK_APP=listed.app:app flask run -p 8080
```

### Result

[![listed-home](https://raw.githubusercontent.com/sayanarijit/listed/master/screenshots/listed-home.png)](http://localhost:8080)
