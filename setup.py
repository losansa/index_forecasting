from setuptools import setup

setup(
   name='index_forecasting',
   version='0.1',
   description='Backend app for quotes forecasting',
   author='Polina',
   packages=['backend'],
   install_requires=['flask',
                     'flask-sqlalchemy',
                     'yfinance',
                     'matplotlib',
                     'psycopg2',
                     'flask_script',
                     'flask_migrate',
                     'torch',
                     'sklearn',
                     ],
)
