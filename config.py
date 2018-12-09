import os
#from configvar import secret_key, db_setting

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or secret_key
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or db_setting
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

