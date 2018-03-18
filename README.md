# Listed

List and display files in the web

[![PyPI version](https://img.shields.io/pypi/v/listed.svg)](https://pypi.org/p/listed)
[![Build Status](https://travis-ci.org/sayanarijit/listed.svg?branch=master)](https://travis-ci.org/sayanarijit/listed)


### Installation

```
# Install via pip
pip install -U --user listed

# Add some demo files
wget https://raw.githubusercontent.com/sayanarijit/listed/master/demofiles/a.md ~/.listed/a.md
wget https://raw.githubusercontent.com/sayanarijit/listed/master/demofiles/b.txt ~/.listed/b.txt

# Run production instance  (robust WSGI server)
listed run prod

# Or run development instance (for debugging only)
listed run dev   
```


### Configuration

| Config       | Environment variable | Default     |
| ------------ | -------------------- | ----------- |
| File storage | LISTED_STORAGE       | '~/.listed' |
| HTTP port    | LISTED_PORT          | 8080        |


### Run

```
# Production
listed run prod

# Development (debug enabled)
listed run dev
```
