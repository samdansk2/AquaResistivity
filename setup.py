from setuptools import setup, find_packages

setup(
    name='seawater',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'colorama==0.4.6',
        'iniconfig==2.0.0',
        'numpy==1.26.4',
        'packaging==23.2',
        'pandas==2.0.3',
        'pluggy==1.4.0',
        'pytest==8.0.1',
        'python-dateutil==2.8.2',
        'pytz==2024.1',
        'six==1.16.0',
        'tzdata==2024.1',
    ],
)
