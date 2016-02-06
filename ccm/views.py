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

def Menu(request):
    if request.method == "GET":
        context = {}
        all_campaigns = Campaign.objects.all()
        campaigns_data = []
        for c in all_campaigns:
            new_c = {}
            new_c["title"] = c.title
            new_c["url"] = "/" + c.url + "/"
            campaigns_data.append(new_c)
        context["campaigns"] = campaigns_data
        return render(request, 'menu.html', context)
    else:
        return HttpResponseRedirect('/menu/')
        
def MLK(request):
    return Home(request, "MLK events -- Reflection on Race", "mlk")

def SA(request):
    return Home(request, "Sexual Assault Awareness at CMU", "sa")

def Home(request, ctitle, curl):
    if request.method == "GET":
        context = {}
        c = Campaign.objects.get(url=curl)
        context["campaign_title"] = c.title
        context["campaign_url"] = c.url
        context["campaign_content"] = c.content
        context["campaign_organizers"] = c.organizers
        
        virtualGoals_data = []
        for vg in VirtualGoal.objects.filter(campaign=c):
            new_vg = {}
            new_vg["title"] = vg.title
            new_vg["content"] = vg.content
            new_vg["datetime"] = vg.datetime
            new_vg["link"] = vg.link
            virtualGoals_data.append(new_vg)
        
        physicalGoals_data = []
        for pg in PhysicalGoal.objects.filter(campaign=c):
            new_pg = {}
            new_pg["title"] = pg.title
            new_pg["content"] = pg.content
            new_pg["datetime"] = pg.datetime
            new_pg["location"] = pg.location
            physicalGoals_data.append(new_pg)
        
        context["physicalGoals"] = physicalGoals_data
        context["virtualGoals"] = virtualGoals_data        
        return render(request, 'home.html', context)
    else:
        data = dict(request.POST)
        if "suggest" in data:
            content = data["suggest"]
            campaign = Campaign.objects.filter(url=curl)[0]
            email = data["email"]
            s = Suggestion(content=content, useremail=email, campaign=campaign)
            s.save()
            
        return HttpResponseRedirect('/'+ curl + "/")

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
    
def getGoalsAchieved(part,physicalgoals_data):
	result=[]
	for goal in physicalgoals_data:
		participants=goal['participants']
		if part in participants:
			result.append(goal)
	return result