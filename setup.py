
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
BINDIR = 'bin'
config = {
    'description': 'secret_details',
    'author': 'Eran Zimbler',
    'url': 'https://github.com/srgrn/secrets_details',
    'author_email': 'eranz@rumble.me',
    'version': '0.3',
    'install_requires': ['nose'],
    'packages': ['secrets_details'],
    'scripts': ['{}/{}'.format(BINDIR,x) for x in os.listdir(BINDIR)],
    'name': 'secret_details'
}

setup(**config)
