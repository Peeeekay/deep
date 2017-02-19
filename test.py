import json
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.encoding import force_text
from chatterbot.ext.django_chatterbot.views import ChatterBotView
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client
from authentication.views import Link
class ApiTestCase(TestCase):
    """
    Tests to make sure that the ChatterBot app is
    properly working with the Django example app.
    """

    def setUp(self):
        super(ApiTestCase, self).setUp()
        self.api_url = reverse('test')

    def test_post(self):
        """
        Test that a response is returned.
        """
        Link.objects.create(name="yo",url="www.random.com",program="ECE",number="106")

        Link.objects.create(name="abc",url="www.abc.ca",program="ECE",number="106")
        user = Client()
        data = {
            'text': 'ECE 106'
        }
        response = user.post(reverse('test'),data)
           

        print (response.content)
        
        

   



