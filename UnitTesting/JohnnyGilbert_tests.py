#How to Run: make sure the test file is in the same directory as the manage.py
#make sure this file name is tests.py
#Test: python3 manage.py test
#Name: Johnny Gilbert
from django.test import TestCase
from myapp.models import Hobby, Sprite, HobbyTime
from django.db import models
from django.contrib.auth.models import User

class BasicTest(TestCase):
    def test_fields(self):
        sprite = Sprite.objects.create(spriteName = "alien")
        user = User.objects.create(username = "JohnnyGilbert57")
        hobby = Hobby()
        hobby.hobbyUser = user
        hobby.spriteId = sprite
        hobby.name = "WorkOut"
        hobby.timeLimit = 3
        hobby.save()
        record = Hobby.objects.get(pk=1)
        self.assertEqual(record, hobby)

