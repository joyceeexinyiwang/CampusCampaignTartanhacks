from django.shortcuts import render

# Create your views here.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ccm.models import *
from tartanhack import settings
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

#helper that gets the title of each link. adapted from https://docs.python.org/3.5/howto/urllib2.html
import json, urllib
#import urllib.request
#from http import client as Client

def Home(request):
    if request.method == "GET":
        context = {}
        #context["campaign_title"] = Campaign.objects.all()[0].title
        #context["campaign_content"] = Campaign.objects.all()[0].content
        all_organizers = Organizer.objects.all()
        all_participants = Participant.objects.all()
        all_physicalGoals = PhysicalGoal.objects.all()
        all_virtualGoals = VirturalGoal.objects.all()
        
        physicalgoals_data = []
        for pg in all_physicalGoals:
            new_pg = {}
            new_pg["content"] = pg.content
            new_pg["datetime"] = pg.datetime
            new_pg["location"] = pg.location
            new_pg["participants"] = pg.split(",") #participants name can't have ","
            new_pg["num_of_participants"] = str(length(pg.split(",")))
            new_pg["achieved"] = pg.achieved
            physicalgoals_data.append(new_pg)

        virturalgoals_data = []
        for vg in all_virtualGoals:
            new_vg = {}
            new_vg["content"] = vg.content
            new_vg["datatime"] = vg.datetime
            new_vg["platform"] = vg.platform
            new_vg["participants"] = vg.split(",") #participants name can't have ","
            new_vg["num_of_participants"] = str(length(vg.split(",")))
            new_vg["achieved"] = vg.achieved
            virturalgoals_data.append(new_vg)
        
        organizers_data = []
        for organizer in all_organizers:
            new_organizer = {}
            new_organizer["name"] = organizer.name
            new_organizer["phone"] = organizer.phone
            new_organizer["occupation"] = organizer.occupation
            organizer_data.append(new_organizer)
            
        participants_data = []
        for participant in all_participants:
            new_participant = {}
            new_participant["name"] = participant.name
            new_participant["phone"] = participant.phone
            new_participant["occupation"] = participant.occupation
            participant_data.append(new_participant)
            
        context["physicalgoals"] = physicalgoals_data
        context["virturalgoals"] = virturalgoals_data
        context["organizers"] = organizers_data
        context["participants"] = participants_data
        return render(request, 'home.html', context)
    else:
        
        return HttpResponseRedirect('/')

def findParticipant(goalDict):
    result = {}
    for goal in goalDict:
        participants = goalDict[goal]
        for participant in participants:
            if participant not in result:
                result[participant] = list()
            if goal not in result[participant]:
                result[participant].append(goal)
    return result
    
