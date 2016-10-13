from distutils.core import setup
from setuptools import setup, find_packages


setup(
    name = 'flasksr',
    packages=find_packages(exclude=('tests', 'tests.*')),
    version = '0.1',
    description = 'An easy way to stream HTTP Responses for Flask and improve time for First Paint',
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
