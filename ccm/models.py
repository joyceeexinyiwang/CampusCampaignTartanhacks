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
    url = models.CharField(max_length=10, default="")
    title = models.CharField(max_length=1000, default="")
    content = models.CharField(max_length=1000, default="")
    organizers = models.CharField(max_length=1000, default="")
    
    def __id__(self):
        return self.title
    """
    def __eq__(self, other):
        return self.title == other.title
    """
    
    def __str__(self):
        return self.title

"""
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

"""
#the naming is bad here...

#physicalGoals mean -- physical events, involvement that happens in the real world.
class PhysicalGoal(models.Model):
    title = models.CharField(max_length=1000, default="")
    content = models.CharField(max_length=1000, default="")
    datetime = models.CharField(max_length=1000, default="")
    location = models.CharField(max_length=1000, default="")
    campaign = models.ForeignKey("Campaign", default="")
    
    def __id__(self):
        return self.title

    def __str__(self):
        return self.title
    
#virtualGoals mean -- virtural events, politival involvement that happens on social media,
#                       circulating an article
class VirtualGoal(models.Model):
    title = models.CharField(max_length=1000, default="")
    content = models.CharField(max_length=1000, default="")
    datetime = models.CharField(max_length=1000, default="")
    link = models.CharField(max_length=1000, default="")
    campaign = models.ForeignKey("Campaign", default="")

    def __id__(self):
        return self.title
        
    def __str__(self):
        return self.title

class Suggestion(models.Model):
    campaign = models.ForeignKey("Campaign", default="")
    content = models.CharField(max_length=1000, default="")
    useremail = models.CharField(max_length=1000, default="")