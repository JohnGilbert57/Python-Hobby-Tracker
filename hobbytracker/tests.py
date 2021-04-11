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
class SpriteTest(TestCase):
    def test_fields(self):
        sprite = Sprite()
        sprite.spriteName = "alien"
        sprite.imageName = "alienImage"
        sprite.save()
        record = Sprite.objects.get(pk=1)
        self.assertEqual(record, sprite)
class HobbyTest(TestCase):
    def test_fields(self):
        hobbyTime = HobbyTime()
        user = User.objects.create(username = "JohnnyGilbert57")
        sprite = Sprite.objects.create(spriteName = "alien")
        hobbyTime.hobby = Hobby.objects.create(hobbyUser = user, name = "Workout", timeLimit = 1, spriteId = sprite)
        hobbyTime.startTime = 1
        hobbyTime.endTime = 2
        hobbyTime.save()
        record = HobbyTime.objects.get(pk=1)
        self.assertEqual(record, hobbyTime)
