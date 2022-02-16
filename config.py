import os




class Config:
    SECRET_KEY = 'mysecretket'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:lilian@localhost/nashlil'

    


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

config_options = {

    'development': DevConfig,
    'production': ProdConfig,
  

}