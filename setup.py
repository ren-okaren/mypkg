from glob import glob
import os

from setuptools import find_packages, setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ren',
    maintainer_email='renrenda77@gmail.com',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',
            'listener = mypkg.listener:main',
            'talker_topic = mypkg.talker_topic:main',
            'listener_topic = mypkg.listener_topic:main',
            'wareki_converter = mypkg.wareki_converter:main',
            'year_pub = mypkg.year_pub:main',
            'wareki_server = mypkg.wareki_server:main',
        ],
    },
)
