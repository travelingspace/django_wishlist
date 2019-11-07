from django.test import TestCase
from django.urls import reverse

from .models import Place
# Create your tests here.

class TestHomePageIsEmptyList(TestCase):
    
    def test_load_home_page_shows_empty_list(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response('travel_wishlist/wishlist.html'))
        self.assertFalse(response.context['places'])
        self.assertContains(response, 'You have no places in your wishlist')