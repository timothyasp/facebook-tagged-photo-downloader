try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Personal Facebook Backup',
    'author': 'Timothy Asp',
    'url': 'https://github.com/timothyasp/fbackup',
    'download_url': 'https://github.com/timothyasp/fbackup',
    'author_email': 'timothy.asp@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'facepy'],
    'packages': ['fbackup'],
    'name': 'fbackup'
}

setup(**config)
