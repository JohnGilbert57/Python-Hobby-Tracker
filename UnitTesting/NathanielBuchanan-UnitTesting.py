# Nathaniel Buchanan
# python3 manage.py test
# Unit Testing on the Sprite Model
from django.test import TestCase
from myapp.models import Hobby, Sprite, HobbyTime
from django.db import models
from django.contrib.auth.models import User

class SpriteTest(TestCase):
    def test_fields(self):
        sprite = Sprite()
        sprite.spriteName = "Rufus"
        sprite.imageName = "rufus_content.jpg"
        sprite.save()
        record = Sprite.objects.get(pk=1)
        self.assertEqual(record, sprite)
