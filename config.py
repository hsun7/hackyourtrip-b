import os
from configvar import secret_key, db_setting

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = secret_key
    SQLALCHEMY_DATABASE_URI = db_setting['uri']
    SQLALCHEMY_TRACK_MODIFICATIONS = db_setting['mod']


