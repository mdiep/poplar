"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


class PoplarViewTests(TestCase):
    urls = 'poplar.urls'
    
    def setUp(self):
        User.objects.create_user(username='spiderman', password='uncleben', email='peterparker@nyu.edu')
    
    def tearDown(self):
        pass
    
    def test_person_list(self):
        """
        Tests the behavior of /people/
        """
        response = self.client.get(reverse('everyone'))
        self.assertEquals(response.status_code, 302)
        
        self.client.login(username='spiderman', password='uncleben')
        response = self.client.get(reverse('everyone'))
        self.assertEquals(response.status_code, 200)

