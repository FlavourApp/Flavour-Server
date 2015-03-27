from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http import HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.views.decorators.http import *
from forms import *
from db.models import *
import data_views
import requests
import hashlib
import hmac
import json
json_serializer = serializers.get_serializer('json')()
import sys

my_reciever_id = '23003'
secret = '9fa9cc61f7455f4ba3345bd7719ebe5cc9afc0e5' 

def emailtest(request):
	msg = "Este es un mensaje de prueba"
	send_mail(
			'flavourapp', 
			msg, 
			'flavourapp@gmail.com',
			('ro3rto@gmail.com','demianschkolnik@gmail.com'), 
			fail_silently=False
		)

@require_POST
def home(request):
	form = ComunaForm(request.POST)
	if form.is_valid():
		comuna = form.cleaned_data['comuna']
		chefs = Chef.objects.filter(comunas__name=comuna)
		return render(request, 'chefs.html', {'chefs':chefs})
	
	form = ComunaForm()
	return render(request, 'home.html', {'form':form})

@csrf_exempt
@require_POST
def pay_khipu(request):
	#parametros POST: chefID, menu, date, usermail
	chefId 			= request.POST.get('chefId')
	menuId 			= request.POST.get('menuId')
	cantidad 		= request.POST.get('cantidad')
	dateId 			= request.POST.get('dateId')
	usermail 		= request.POST.get('payerEmail')
	username 		= request.POST.get('userName')
	useraddress 	= request.POST.get('userAddress')
	userphone 		= request.POST.get('userPhone')
	body 			= Menu.objects.get(pk=menuId).description

	reserva = Reserva(
			chef 			= Chef.objects.get(pk=chefId),
			usermail 		= usermail,
			menu 			= Menu.objects.get(pk=menuId),
			cantidad 		= cantidad,
			date 			= '2014-10-10',
			status 			= 'unverified',
			username 		= username,
			useraddress 	= useraddress,
			userphone 		= userphone,

		)

	#reserva.status 		= 'Unverified'
	reserva.save()

	#hacemos llamada a khipu
	url = 'https://khipu.com/api/1.3/createPaymentURL'
	#parametros

	amount = str(int(reserva.cantidad)* int(reserva.menu.precio))
	parameters = [
		('receiver_id' 		, my_reciever_id),
		('subject' 			, 'Compra en Flavour'),
		('body' 			, str(body)),
		#('amount' 			, str(int(reserva.menu.precio) * int(reserva.cantidad))), 
		('amount'		, amount),
		('payer_email' 		, usermail),
		('bank_id' 			, ''),
		('expires_date' 	, ''),
		('transaction_id' 	, str(reserva.pk)),
		('custom' 			, ''),
		('notify_url' 		, 'http://54.69.134.41:80/successfulPayment/'),
		('return_url' 		, 'flavour://success.flavour.com'),
		('cancel_url' 		, 'flavour://failure.flavour.com'),
		('picture_url' 		, ''),
	]
	#concatenamos para el requisito del parametro hash
	concatenated_list = [key + "=" + value for key,value in parameters]
	concatenated = "&".join(concatenated_list)
	#calculamos el parametro hash
	hash_parameter = hmac.new(secret, msg=concatenated, digestmod=hashlib.sha256).hexdigest()
	#mandamos request a khipu
	parameters.append(('hash', hash_parameter))
	data = dict(parameters)
	req = requests.post(url, data=data)
	if req.text:
		print request.POST
		#return HttpResponse(str(request.POST))
		#return HttpResponse(str(amount) + ' ' + req.text)
		#enviamos el parametro mobile-url al cliente
		mobile_url =req.json()['mobile-url']
		return HttpResponse(
			json.dumps(
				{'mobile-url' : mobile_url}
			), 
			content_type="application/json")

@csrf_exempt
@require_POST
def sucsessful_payment(request):
	#debemos verificar que es khipu quien notifica de un pago exitoso
	verification_url = 'https://khipu.com/api/1.3/verifyPaymentNotification'
	parameters = [
					'api_version', 'receiver_id', 'notification_id', 
					'subject', 'amount', 'currency', 'transaction_id', 
					'payer_email', 'custom'
				]
	data = {}

	for param in parameters:
		data[param] = request.POST[param]
	 	

	data['notification_signature'] = request.POST['notification_signature']
	req = requests.post(verification_url, data=data)
	reserva = Reserva.objects.get(
				pk 	= request.POST['transaction_id'],
			)
	#if req.text == 'VERIFIED' and reserva.status == 'unverified' and request.POST['receiver_id'] == my_reciever_id:
	if True:	#una vez verificado procedemos a realizar la reserva en el sistema
					
		reserva.status = 'verified'

		#mail al usuario
		msg = "Hola, muchas gracias por usar FlavourApp.\n"
		msg += "Los detalles de su pedido son:\nChef: {}\nMenu: {}\nPrecio: {}\nFecha: {}".format(
				reserva.chef.name + " " + reserva.chef.lastname,
				reserva.menu.name,
				'$'+ str(reserva.menu.precio * reserva.cantidad),
				reserva.date
			)

		send_mail(
			'flavourapp', 
			msg, 
			'flavourapp@gmail.com',
			(reserva.usermail,), 
			fail_silently=False
		)

		#mail al chef

		msg = "Estimado {}, le informamos que se ha realizado un pedido para el dia {} del menu {} para {} personas.\nLos datos de contacto son los siguientes:\nNombre: {}\n Telefono: {}\n direccion: {}\n Mail: {}".format(
				reserva.chef.name + " " + reserva.chef.lastname,
				str(reserva.date),
				reserva.menu.name,
				reserva.cantidad,
				reserva.username,
				reserva.userphone,
				reserva.useraddress,
				reserva.usermail,
			)

		send_mail(
			'flavourapp', 
			msg, 
			'flavourapp@gmail.com',
			(reserva.chef.email,), 
			fail_silently=False
		)


		return HttpResponse(
		json.dumps(
			[]
		), 
		content_type="application/json")		

	return HttpResponse(
			json.dumps(
				[]
			), 
			content_type="application/json")


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
