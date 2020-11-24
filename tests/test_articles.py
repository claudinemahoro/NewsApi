import unittest
from app.models import Articles

class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Articles('Claudine','News','Science','https://google.com','https://google.com/images','2020-11-24 T13:31:03Z')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
    
    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.author,'Claudine')
        self.assertEquals(self.new_article.title,'News')
        self.assertEquals(self.new_article.description,'Science is driving the world ahead')
        self.assertEquals(self.new_article.url,'https://google.com')
        self.assertEquals(self.new_article.urlToImage,'https://google.com/images')
        self.assertEquals(self.new_article.publishedAt,'2020-11-24 T13:31:03Z')