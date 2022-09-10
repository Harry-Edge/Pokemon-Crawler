from django.test import TestCase
import requests


class TestIndexViews(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_method(self):
        response = self.client.post('/')
        self.assertEqual(response.status_code, 302)

