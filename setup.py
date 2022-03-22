import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'requests == 2.*',
]

DEV_REQUIREMENTS = [
    'black',
    'coveralls == 3.*',
    'flake8',
    'isort',
    'mypy',
    'pytest == 7.*',
    'pytest-cov == 3.*',
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
    packages=setuptools.find_packages(),
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
