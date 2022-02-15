import os
os.urandom(24)

class Config:
    # SECRET_KEY = 'mysecretket'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:lilian@localhost/apostgre'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI =os.environ.get('SQLALCHEMY_DATABASE_URI')
  


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
