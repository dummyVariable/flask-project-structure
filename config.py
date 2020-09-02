import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config():

    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASEDIR}/data.db'
    SQLALCHEMY_TRACE_MODIFICATIONS = False
    