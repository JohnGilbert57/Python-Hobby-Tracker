# Johnny Gilbert
# Ohio University
# template for meta-data; defines the variables for the Hobby and the User
from django.db import models
from django import forms

class HobbyUser(models.Model):
    # Data fields
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    userName = models.CharField(max_length=200)
    password = models.CharField(max_length=50)

    # Called when displaying raw data
    def __str__(self):
        return self.userName + " - " + self.firstName + " " + self.lastName

class Hobby(models.Model):
    # Establish a foreign key relationship with HobbyUser
    hobbyUser = models.ForeignKey(HobbyUser, on_delete=models.CASCADE)

    # Data fields
    name = models.CharField(max_length=300)
    spriteId = models.IntegerField()

    # Called when displaying raw data
    def __str__(self):
        return self.name

class HobbyTime(models.Model):
    # Establish a foreign key relationship with Hobby
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)

    # Data fields
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
