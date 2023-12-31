from django.test import TestCase

from .models import Puppy


class PuppyTest(TestCase):
    def setUp(self) -> None:
        Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppy.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')

    def test_puppy_breed(self):
        puppy_casper = Puppy.objects.get(name='Casper')
        puppy_muffin = Puppy.objects.get(name='Muffin')
        self.assertEqual(
            puppy_casper.get_bread(), 'Bull Dog')
        self.assertEqual(
            puppy_muffin.get_bread(), 'Gradane')
