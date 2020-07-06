import os

class Configuration():
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'postgresql://pyweb_test_user:pyweb@localhost/pyweb_test_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
