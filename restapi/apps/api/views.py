from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.utils import simplejson

from apps.core.models import *

def teams(request):
    teams_array = []

    teams = Team.objects.all()
    
    for team in teams:
        teams_array.append(model_to_dict(team, exclude=['id']))
        
    teams_dict = {
        'status':200,
        'teams' : teams_array
    }
    json = simplejson.dumps(teams_dict)
    return HttpResponse(json, content_type='application/json')