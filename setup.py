
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'secret_details',
    'author': 'Eran Zimbler',
    'url': 'https://github.com/srgrn/secrets_details',
    'author_email': 'eranz@rumble.me',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['secrets_details'],
    'scripts': ['bin/ProvExplorer'],
    'name': 'secret_details'
}

setup(**config)
