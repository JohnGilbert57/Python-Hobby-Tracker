from django.test import TestCase
from myapp.models import Hobby, Sprite, HobbyTime
from django.db import models
from django.contrib.auth.models import User

#How to Run: make sure the test file is in the same directory as the manage.py
#make sure this file name is tests.py
#Test: python3 manage.py test
#Name: Spencer Deuscher

class HobbyTest(TestCase):
    def test_fields(self):
        hobbyTime = HobbyTime()
        user = User.objects.create(username = "SDeuscher")
        sprite = Sprite.objects.create(spriteName = "Rufus", imageName = "RufusImage")
        hobbyTime.hobby = Hobby.objects.create(hobbyUser = user, name = "Soccer", timeLimit = 1, spriteId = sprite)
        hobbyTime.startTime = "2021-04-12 06:27"
        hobbyTime.endTime = "2021-04-12 07:27"
        hobbyTime.save()
        record = HobbyTime.objects.get(pk=1)
        self.assertEqual(record, hobbyTime)
