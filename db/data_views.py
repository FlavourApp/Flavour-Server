from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core import serializers
from forms import *
from db.models import *

import json
json_serializer = serializers.get_serializer('json')()

def chefs(request):
	if request.method == 'GET':
		comuna = request.GET['comuna']

		chef_list = Chef.objects.filter(comunas__name__contains=comuna)

		return HttpResponse(
				json_serializer.serialize(chef_list), 
				content_type="application/json"
			)

def dates(request):
	if request.method == 'GET':
		pk = request.GET['chefId']
		dates = {
			"dates": [str(date.date) for date in Date.objects.filter(chef__pk=pk)]
		}
		return HttpResponse(json.dumps(dates), content_type="application/json")
	else:
		return HttpResponse('Error')

def menus(request):
	if request.method == 'GET':
		pk = request.GET['chefId']
		menus = Menu.objects.filter(chef__pk=pk)
		return HttpResponse(
				json_serializer.serialize(menus), 
				content_type="application/json"
			)
	else:
		return HttpResponse('Error')