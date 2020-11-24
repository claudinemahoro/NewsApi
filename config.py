import os

class Config:
    '''
    General configuration for the parent class
    '''
    
    SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey=42193a34df054c76a2fd24f0d12cfc4c'
    ARTICLES_BASE_URL ='https://newsapi.org/v2/everything?sources=bbc-news&apiKey=42193a34df054c76a2fd24f0d12cfc4c'
    NEWS_API_KEY = '42193a34df054c76a2fd24f0d12cfc4c'
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