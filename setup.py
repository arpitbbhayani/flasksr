from distutils.core import setup
from setuptools import setup, find_packages


setup(
    name = 'flasksr',
    packages=find_packages(exclude=('tests', 'tests.*')),
    version = '0.6',
    description = 'Start streaming HTTP Responses based on your page layout for Flask and improve Time for First Paint.',
    author = 'Arpit Bhayani',
    author_email = 'arpit.bhayani@gmail.com',
    url = 'https://github.com/arpitbbhayani/flasksr',
    download_url = 'https://github.com/arpitbbhayani/flasksr',
    keywords = ['flask', 'response', 'fast website', 'fast page load'],
    install_requires=[
        'flask>=0.1',
    ],
    classifiers = [],
)
