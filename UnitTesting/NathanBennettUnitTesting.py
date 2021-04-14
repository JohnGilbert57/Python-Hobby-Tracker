from django.test import TestCase
from myapp.models import Hobby, Sprite, HobbyTime
from django.db import models
from django.contrib.auth.models import User

# Nathan Bennett
# Unit Testing as a BasicTest
class BasicTest(TestCase):
    def test_fields(self):
        sprite = Sprite().objects.create(spriteName = "babyYoga")
        user = User.objects.create(username = "NBennett2019")
        hobby = Hobby()
        hobby.hobbyUser = user
        hobby.spriteId = sprite
        hobby.name = "Play Guitar"
        hobby.timeLimit = 3
        hobby.save()
        record = Hobby.objects.get(pk = 1)
        self.assertEqual(record, hobby)