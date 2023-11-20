import os
import glob
from setuptools import find_packages, setup

package_name = 'phidget_stepper_controllers'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #(os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), ['config/tests.yaml'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='remi',
    maintainer_email='remipbw@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test_speed = phidget_stepper_controllers.test_speed:main',
            'test_step = phidget_stepper_controllers.test_step:main'
        ],
    },
)
