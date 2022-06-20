from setuptools import setup, find_packages

setup(
    name='csCore',
    description='Core library for Common Stocks Application',
    version='0.0.1',
    author='James Dooley',
    author_email='james@developernotes.org',
    packages=find_packages(exclude=('test',)),
    install_requires=[
        'attrs>=21.4.0',
        'pendulum>=2.1.2',
        'orjson>=3.7.2'
    ],
    url='https://www.developernotes.org'
)
