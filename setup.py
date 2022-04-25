from setuptools import setup, find_packages

setup(
    name='walldisplay-calendar',
    version="0.3",
    author='GEANT',
    author_email='swd@geant.org',
    description='skeleton flask react app',
    url=('TBD'),
    packages=find_packages(),
    install_requires=[
        'jsonschema',
        'flask',
        'flask-cors',
        'requests',
        'python-dateutil'
    ],
    include_package_data=True,
)
