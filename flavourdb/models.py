from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=200, default = '')
	surName = models.CharField(max_length=200, default = '')

class Chef(models.Model):
	name = models.CharField(max_length=60, default = '')
	lastname = models.CharField(max_length=60, default = '')
	email = models.EmailField(max_length=60)
	phone = models.CharField(max_length=12)
	pictureUrl = models.URLField(max_length=200)
	description = models.CharField(max_length=200, default='')

class Comuna(models.Model):
	name = models.CharField(max_length=60, default = '')
	chefs = models.ManyToMany(Chef)

class ChefBioFoodImage(models.Model):
	url = models.URLField(max_length=200)
	chef = models.ForeignKey(Chef)

class Menu(models.Model):
	description = models.CharField(max_length=200, default='')
	precio = models.IntegerField(default=0)
	preparationTime = models.IntegerField(default=0)

class MenuImage(models.Model):
	url = models.URLField(max_length=200)
	menu = models.ForeignKey(Menu)

