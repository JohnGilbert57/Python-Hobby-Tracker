from django.test import TestCase
from myapp.models import Hobby, Sprite, HobbyTime
from django.db import models
from django.contrib.auth.models import User

# Taylor Miller
# Unit Testing on the Sprite Model
class SpriteTest(TestCase):
    def test_fields(self):
        sprite = Sprite()
        sprite.spriteName = "LandShark"
        sprite.imageName = "LandShark_happy.jpg"
        sprite.save()
        record = Sprite.objects.get(pk = 1)
        self.assertEqual(record,sprite)