from django.db import models
import time

# Create your models here.

class User(models.Model):
	name 	= models.CharField(max_length=200, default = '')
	surName = models.CharField(max_length=200, default = '')

class Comuna(models.Model):	
	name 	= models.CharField(max_length=60, default = '', primary_key=True)

	def __unicode__(self):
		return "{}".format(self.name)

class Chef(models.Model):
	name 		= models.CharField(max_length=60, default = '')
	lastname 	= models.CharField(max_length=60, default = '')
	email 		= models.EmailField(max_length=60)
	phone 		= models.CharField(max_length=12)
	picture 	= models.ImageField(default = '')
	description = models.CharField(max_length=200, default='')
	comunas 	= models.ManyToManyField(Comuna)
	bio 		= models.CharField(default= '',max_length=255)


	def image_tag(self):
		return u'<image src="%s" />' % self.picture.url
		image_tag.short_description = 'Image'
		image_tag.allow_tags = True

	def __unicode__(self):
		return "{} {} | {}".format(self.name, self.lastname, self.description)

class Consumer(models.Model):
	name 		= models.CharField(max_length=60, default = '')
	lastname 	= models.CharField(max_length=60, default = '')
	address 	= models.CharField(max_length=60, default = '')
	phone 		= models.CharField(max_length=12, default = '')
	FBID 		= models.CharField(max_length=60, default = '', blank=True)
	email 		= models.EmailField(max_length=60, default = '')
	comuna 		= models.ForeignKey(Comuna)	

class ChefBioFoodImage(models.Model):
	url 	= models.URLField(max_length=200)
	chef 	= models.ForeignKey(Chef)

	def __unicode__(self):
		return "{}".format(self.url)

class Menu(models.Model):
	name 			= models.CharField(max_length=200, default='')
	description 	= models.CharField(max_length=200, default='')
	precio 			= models.IntegerField(default=0)
	preparationTime = models.IntegerField(default=0)
	picture 		= models.ImageField(max_length=200, default='')
	chef 			= models.ForeignKey(Chef)
	tipo 			= models.CharField(max_length=200, default='')

	def __unicode__(self):
		return "${} | {}".format(self.precio, self.description)

class Date(models.Model):
	chef = models.ForeignKey(Chef) 
	date = models.DateField(default = "2015-10-10")

	def __unicode__(self):
		return "Chef: {} Fecha: {}".format(
				self.chef.name,
				self.date
			)

class Reserva(models.Model):
	chef 			= models.ForeignKey(Chef)
	usermail 		= models.CharField(max_length=60)
	menu 			= models.ForeignKey(Menu)
	cantidad 		= models.IntegerField(default= 1)
	date 			= models.DateField(default= "2015-10-10")
	status 			= models.CharField(max_length=60)
	username 		= models.CharField(max_length=60)
	useraddress 	= models.CharField(max_length=60)
	userphone 		= models.CharField(max_length=60)


	def __unicode__(self):
		return "chef: {}, menu: {}, date: {}".format(
				self.chef.name, self.menu.name, self.date
			)



class MenuImage(models.Model):
	url 	= models.URLField(max_length=200)
	menu 	= models.ForeignKey(Menu)

	def __unicode__(self):
		return "{}".format(self.url)