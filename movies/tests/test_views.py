from django.test import Client
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..models import Puppy
from ..serializers import PuppySerializer

client = Client()


class GetAllPuppiesTest(TestCase):
    def setUp(self) -> None:
        Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppy.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')

    def test_get_all_puppies(self):
        response = client.get(reverse('get_post_puppies'))
        puppies = Puppy.objects.all()
        print(puppies)
        print(response)

        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
