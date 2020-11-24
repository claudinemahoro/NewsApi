import urllib.request,json
from .models import Sources,Articles

# News = news.News

# Getting api key
api_key = None
sources_url = None
articles_url = None

def configure_request(app):
    global api_key, sources_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']

