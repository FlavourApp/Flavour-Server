from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core import serializers
from django.views.decorators.http import *
from forms import *
from db.models import *

import json
json_serializer = serializers.get_serializer('json')()

@require_GET
def chefs(request):
	comuna = request.GET['comuna']
	chef_list = Chef.objects.filter(comunas__name__contains=comuna)
	return HttpResponse(
			json_serializer.serialize(chef_list), 
			content_type="application/json"
		)
@require_GET
def dates(request):
	pk = request.GET['chefId']	
	dates = Date.objects.filter(chef__pk=pk)
	return HttpResponse(json_serializer.serialize(dates), content_type="application/json")

@require_GET
def reservations(request):
	reserva = Reserva.objects.get(pk=request.GET['pk'])
	return HttpResponse(json.dumps(reserva), content_type="application/json")

@require_GET
def menus(request):
	pk = request.GET['chefId']
	menus = Menu.objects.filter(chef__pk=pk)
	return HttpResponse(
			json_serializer.serialize(menus), 
			content_type="application/json"
		)
