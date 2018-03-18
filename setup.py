from setuptools import setup, find_packages
from codecs import open
from os import path
from listed.config import VERSION

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Requirements for installation
with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name='listed',
    version=VERSION,

    description='List and display files in the web',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Arijit Basu',
    author_email='sayanarijit@gmail.com',

    url='https://github.com/sayanarijit/listed',
    # download_url='https://github.com/sayanarijit/listed/archive/{}.tar.gz'.format(VERSION),

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.2',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Environment :: Console',
        'Operating System :: POSIX'
    ],

    scripts=[],

    provides=[],
    install_requires=install_requirements,

    namespace_packages=[],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'listed-dev = listed.server:dev',
            'listed-prod = listed.server:prod'
        ],
    },

    zip_safe=False,
)
