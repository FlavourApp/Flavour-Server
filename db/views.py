from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http import HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
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

@csrf_exempt
def reserva(request):
	if request.method == 'POST':
		print request.POST
		form = ReservaForm(request.POST)
		if form.is_valid():
			form.save()

			msg ='''
			Hola, muchas gracias por ordenar usando FlavourApp
			los detalles de su pedido son:

			Chef: {}
			Menu: {}
			Precio: {}
			Fecha: {}

			''' . format(
				Chef.objects.get(pk=request.POST['chef']).name +
				Chef.objects.get(pk=request.POST['chef']).lastname,
				Menu.objects.get(pk=request.POST['menu']).name,
				'$'+str(Menu.objects.get(pk=request.POST['menu']).precio),
				request.POST['date']
				)

			send_mail(
				'flavourapp', 
				msg, 
				'flavourapp@gmail.com',
    		(request.POST['usermail'],), 
    		fail_silently=False
    	)
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