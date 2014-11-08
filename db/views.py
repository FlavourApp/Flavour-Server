from django.shortcuts import render
from django.http import HttpResponse

import json

from db.models import *
from django.core import serializers

JSONserializer = serializers.get_serializer('json')
json_serializer = JSONserializer()

def mainView(request):

	idUser = int(request.GET.get('userId', -1))
	if idUser == '':
		pass #TODO return something client understands
	comuna = Consumer.objects.filter(pk=idUser)[0].comuna
	allChefs = Chef.objects.filter(comunas__name=comuna)

	response_data = {}
	chef_list = []
	response_data['chefs'] = chef_list

	for chef in allChefs:
		chef_dict ={}
		chef_dict['name'] = chef.name
		chef_dict['lastname'] = chef.lastname
		chef_dict['pictureUrl'] = chef.pictureUrl
		chef_dict['description'] = chef.description
		chef_list.append(chef_dict)

	return HttpResponse(json.dumps(
			response_data), 
			content_type="application/json"
		)

def addConsumer(request):

	name = request.POST.get('name')
	lastname = request.POST.get('lastname')
	address = request.POST.get('address')
	phone = request.POST.get('phone')
	FBID = request.POST.get('FBID')
	email = request.POST.get('email')
	comuna = request.POST.get('comuna')
	comuna = Comuna.objects.filter(name=comuna)[0]
	
	consumer = Consumer(
		name=name,
		lastname=lastname,
		address=address,
		phone=phone,
		FBID = FBID,
		email=email,
		comuna=comuna)
	try:
		consumer.save()	
	except Exception:
		return HttpResponse("failed")
	return HttpResponse("ok")

def chefs(request):
	return HttpResponse(
			json_serializer.serialize(Chef.objects.all()), 
			content_type="application/json"
		)

def dates(request):
	pk = request.GET['chefId']

	dates = {"dates": [str(date.date) for date in Date.objects.filter(chef__pk=pk)]}
	return HttpResponse(json.dumps(dates), content_type="application/json")

def index(request):

	allUsers = User.objects.all()
	response_data = {}
	user_list = []
	response_data['users'] = user_list

	for user in allUsers:
		user_dict ={}
		user_dict['user'] = user.name
		user_dict['surName'] = user.surName
		user_list.append(user_dict)

	return HttpResponse(json.dumps(response_data), content_type="application/json")