from django.test import TestCase
from myapp.models import Hobby, Sprite, HobbyTime
from django.db import models
from django.contrib.auth.models import User
#name: Johnny Gilbert
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
        hobbyTime.startTime = "2021-04-14 07:27"
        hobbyTime.endTime = "2021-04-12 08:00"
        hobbyTime.save()
        record = HobbyTime.objects.get(pk=1)
        self.assertEqual(record, hobbyTime)
# Nathaniel Buchanan
# python3 manage.py test
# Unit Testing on the Sprite Model
class SpriteTest(TestCase):
    def test_fields(self):
        sprite = Sprite()
        sprite.spriteName = "Rufus"
        sprite.imageName = "rufus_content.jpg"
        sprite.save()
        record = Sprite.objects.get(pk=1)
        self.assertEqual(record, sprite)
# Taylor Miller
# Unit Testing on the Sprite Model
class DifferentSpriteTest(TestCase):
    def test_fields(self):
        sprite = Sprite()
        sprite.spriteName = "LandShark"
        sprite.imageName = "LandShark_happy.jpg"
        sprite.save()
        record = Sprite.objects.get(pk = 1)
        self.assertEqual(record,sprite)
#Test: python3 manage.py test
#Name: Spencer Deuscher
class DifferentHobbyTest(TestCase):
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
# Nathan Bennett
# Unit Testing as a BasicTest
class BasicTest(TestCase):
    def test_fields(self):
        sprite = Sprite.objects.create(spriteName = "babyYoga")
        user = User.objects.create(username = "nbennett2019")
        hobby = Hobby()
        hobby.hobbyUser = user
        hobby.spriteId = sprite
        hobby.name = "Play Guitar"
        hobby.timeLimit = 3
        hobby.save()
        record = Hobby.objects.get(pk = 1)
        self.assertEqual(record, hobby)