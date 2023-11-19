from setuptools import find_packages
from setuptools import setup

setup(
    name='phidgets_msgs',
    version='2.3.1',
    packages=find_packages(
        include=('phidgets_msgs', 'phidgets_msgs.*')),
)
