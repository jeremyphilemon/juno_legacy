from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model

from blog.models import Story

User = get_user_model()


class storyCLSTestCase(APITestCase):
    def setUp(self):
        user_obj = User(username="test", email="test@test.com")
        user_obj.set_password("password")
        user_obj.save()
        story = Story.objects.create(title="Testing the title", story="Testing the story")

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_get_list(self):
        data = {}
        url = api_reverse("story-cls")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_list(self):
        data = {"title": "Random title", "story": "Random story"}
        url = api_reverse("story-cls")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
