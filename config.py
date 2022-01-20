import os 

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pytest.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False





