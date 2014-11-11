from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http import HttpResponseRedirect
from django.core import serializers
from forms import *
from db.models import *
import data_views

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

def menus(request, chefid):

	req = HttpRequest()
	req.method = 'GET'
	req.GET = {
		'chefId' :  chefid,
	}
	resp = data_views.menus(req)

	menus = Menu.objects.filter(chef__pk=chefid)

	return render(
			request, 
			'menus.html', 
			{'menus':menus}
		)