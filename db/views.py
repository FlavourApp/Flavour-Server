from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http import HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from forms import *
from db.models import *
import data_views
import requests
import hashlib
import hmac

my_reciever_id = '***'

@require_POST
def home(request):
	form = ComunaForm(request.POST)
	if form.is_valid():
		comuna = form.cleaned_data['comuna']
		chefs = Chef.objects.filter(comunas__name=comuna)
		return render(request, 'chefs.html', {'chefs':chefs})
	
	form = ComunaForm()
	return render(request, 'home.html', {'form':form})

@require_POST
def pay_khipu(request):
	#parametros POST: chefID, menu, date, usermail

	reserva = Reserva(
			chef 		= '',
			usermail 	= '',
			menu 		= '',
			date 		= '',
		)

	reserva.status 		= 'Unverified'
	reserva.trans_id 	= transaction_id

	#hacemos llamada a khipu
	url = 'https://khipu.com/api/1.3/createPaymentURL'
	#parametros
	parameters = [
		('receiver_id' 		= my_reciever_id),
		('subject' 			= 'subject'),
		('body' 			= 'body'),
		('amount' 			= 333),
		('payer_email' 		= 'a@b.com'),
		('bank_id' 			= 333),
		('expires_date' 	= '3/3/3'),
		('transaction_id' 	= 333),
		('custom' 			= 'custom'),
		('notify_url' 		= 'url.notify.com'),
		('return_url' 		= 'url.com'),
		('cancel_url' 		= 'url.com'),
		('picture_url' 		= 'url.com'),
	]
	#concatenamos para el requisito del parametro hash
	concatenated_list = [key + "=" + value for key,value in parameters]
	concatenated = "&".join(concatenated_list)
	#calculamos el parametro hash
	secret = '***'
	hash_parameter = hashed = hmac.new(secret, msg=concatenated, digestmod=hashlib.sha256).digest()
	#mandamos request a khipu
	data = dict(parameters)
	req = requests.post(url, data=data)
	if req.text:
		#enviamos el parametro mobile-url al cliente
		mobile_url =req.json()['mobile-url']

@require_POST
def sucsessful_payment(request):
	#debemos verificar que es khipu quien notifica de un pago exitoso
	verification_url = 'https://khipu.com/api/1.3/verifyPaymentNotification'
	parameters = [
					'api_version', 'receiver_id', 'notification_id', 
					'subject', 'amount', 'currency', 'transaction_id', 
					'payer_email', 'custom'
				]
	data = {
		param : request.POST[param]
	} for param in parameters

	data['notification_signature'] = request.POST['notification_signature']
	req = requests.post(verification_url, data=data)
	if req.test == 'VERIFIED' and receiver_id=my_reciever_id:
		#una vez verificado procedemos a realizar la reserva en el sistema
		try:
			reserva = Reserva.objects.get(
				trans_id 	= request.POST['transaction_id'], 
				custom		= request.POST['custom'], 
				subject 	= request.POST['subject'], 
				amount 		= request.POST['amount']
			)
			reserva.status = 'verified'

			msg = "Hola, muchas gracias por usar FlavourApp.\n"
			msg += "Los detalles de su pedido son:\nChef: {}\nMenu: {}\nPrecio: {}\nFecha: {}".format(
					reserva.chef.name + " " + reserva.chef.lastname,
					reserva.menu.name,
					'$'+ str(reserva.menu.precio),
					reserva.date
				)


			send_mail(
				'flavourapp', 
				msg, 
				'flavourapp@gmail.com',
    			(reserva.usermail,), 
    			fail_silently=False
    		)
		except Reserva.DoesNotExist:
			pass


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