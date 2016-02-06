from __future__ import unicode_literals
import datetime
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.

class Campaign(models.Model):
    title = models.CharField(max_length=1000, default="")
    content = models.CharField(max_length=1000, default="")
    organizers = models.CharField(max_length=1000, default="")
    
    def __str__(self):
        return self.title

class Organizer(models.Model):
    name = models.CharField(max_length=1000, default="")
    phone = models.IntegerField(default=0)
    occupation = models.CharField(max_length=1000, default="")
    
    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name
    

class Participant(models.Model):
    name = models.CharField(max_length=1000, default="")
    phone = models.IntegerField(default=0)
    occupation = models.CharField(max_length=1000, default="")

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name
    
class PhysicalGoal(models.Model):
    content = models.CharField(max_length=1000, default="")
    datetime = models.DateTimeField()
    location = models.CharField(max_length=1000, default="")
    compaign = models.ForeignKey(Campaign, default="")
    participants = models.CharField(Participant, default="")
    achieved = models.BooleanField(default=False)
    

class VirturalGoal(models.Model):
    content = models.CharField(max_length=1000, default="")
    datetime = models.DateTimeField()
    platform = models.CharField(max_length=1000, default="")
    compaign = models.ForeignKey(Campaign, default="")
    participants = models.CharField(Participant, default="")
    achieved = models.BooleanField(default=False)