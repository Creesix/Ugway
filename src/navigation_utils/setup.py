from setuptools import find_packages, setup
import os

package_name = 'navigation_utils'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), ['config/defaultparams.yaml'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='remi',
    maintainer_email='remipbw@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cmd_vel_differential_robot_subscriber = navigation_utils.cmd_vel_differential_robot_subscriber:main'
        ],
    },
)
