import os

class Config:
    '''
    General configuration for the parent class
    '''

    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=5a23e2c7f0b44be49401d6117d5d32db'
    ARTICLES_BASE_URL ='https://newsapi.org/v2/everything?language=en&sources={}&apiKey=5a23e2c7f0b44be49401d6117d5d32db'
    NEWS_API_KEY = '5a23e2c7f0b44be49401d6117d5d32db'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}