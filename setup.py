from distutils.core import setup

setup(
    name='Simperium',
    version='0.0.4',
    author='Andy Gayton',
    author_email='andy@simperium.com',
    package_dir = {'': 'python'},
    packages=['simperium', 'simperium.test'],
    scripts=[],
    # url='http://pypi.python.org/pypi/Simperium/',
    # license='LICENSE.txt',
    description='Python client for the Simperium synchronization platform',
    long_description=open('README.md').read(),
    install_requires=[
    ],
)
