from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core import serializers
from forms import *
from db.models import *

import json
json_serializer = serializers.get_serializer('json')()

def home(request):
	if request.method == 'POST':
		form = ComunaForm(request.POST)
		if form.is_valid():
			comuna = form.cleaned_data['comuna']
			chefs = Chef.objects.filter(comunas__name=comuna)
			return render(request, 'chefs.html', {'chefs':chefs})
	else:
		form = ComunaForm()
	return render(request, 'home.html', {'form':form})

def reserva(request):
	if request.method == 'POST':
		form = ReservaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = ReservaForm()
	return render(request, 'reserva.html', {'form':form})

def chefs(request):
	return HttpResponse(
			json_serializer.serialize(Chef.objects.all()), 
			content_type="application/json"
		)

def dates(request):
	pk = request.GET['chefId']

	dates = {
	"dates": [str(date.date) for date in Date.objects.filter(chef__pk=pk)]
	}
	return HttpResponse(json.dumps(dates), content_type="application/json")