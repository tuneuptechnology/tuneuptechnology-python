import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRES = [
    'requests >= 1.0.0',
]

setuptools.setup(
    name='tuneuptechnology',
    version='2.0.0',
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
    install_requires=REQUIRES,
    extras_require={
        'dev': [
            'flake8 >= 3.8.0',
        ]
    },
    python_requires='>=3.6',
)
