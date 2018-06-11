from setuptools import setup
import os

setup(
    name='hello',
    version='0.1.%s' % os.environ.get('TRAVIS_BUILD_NUMBER', 0),
    description='Hello world example',
    author='Christopher Davies',
    author_email='christopherdavies553@gmail.com',
    license='MIT',
    packages=['hello'],
    zip_safe=False
)