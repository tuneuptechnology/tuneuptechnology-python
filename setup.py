import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'requests == 2.*',
]

DEV_REQUIREMENTS = [
    'black == 22.*',
    'build == 0.7.*',
    'coveralls == 3.*',
    'flake8 == 4.*',
    'isort == 5.*',
    'mypy == 0.942',
    'pytest == 7.*',
    'pytest-cov == 3.*',
    'twine == 4.*',
    'types-requests',
    'vcrpy == 4.*',
]

setuptools.setup(
    name='tuneuptechnology',
    version='3.0.0',
    description='The Python client library for the Tuneup Technology App.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/tuneuptechnology/tuneuptechnology-python',
    author='Tuneup Technology',
    author_email='tuneuptechnology@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(
        exclude=[
            'examples',
            'test',
        ]
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    python_requires='>=3.7, <4',
)
