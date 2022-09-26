
from setuptools import setup


setup(
    name='rc',
    entry_points={
        'console_scripts': [
            'rc=rc.cli:main'
        ],
    },
)
