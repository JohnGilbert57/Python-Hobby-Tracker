# Johnny Gilbert
# Nathaniel Buchanan
# Ohio University
# template for meta-data; defines the variables for the Hobby and the User
from django.db import models
from django import forms
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Hobby(models.Model):
    # Establish a foreign key relationship with HobbyUser
    hobbyUser = models.ForeignKey(User, on_delete=models.CASCADE)

    # Data fields
    name = models.CharField(max_length=300)
    spriteId = models.IntegerField()
    timeLimit = models.IntegerField()

    # Called when displaying raw data
    def __str__(self):
        return "{}-{}".format(self.name, self.time)

class HobbyTime(models.Model):
    # Establish a foreign key relationship with Hobby
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)

    # Data fields
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

class Sprite(models.Model):
    # Data fields
    spriteName = models.CharField(max_length=200)
    imageName = models.CharField(max_length=100)
    # Add or remove fields as needed
