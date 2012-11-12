try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Facebook Photo Downloader',
    'author': 'Timothy Asp',
    'url': 'https://github.com/timothyasp/fb-photo-grab',
    'download_url': 'https://github.com/timothyasp/fb-photo-grab',
    'author_email': 'timothy.asp@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'facepy', 'urllib2'],
    'packages': ['fphoto'],
    'name': 'fphoto'
}

setup(**config)
