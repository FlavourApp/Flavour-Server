from django.contrib import admin

# Register your models here.
from db.models import User, Chef, Comuna, Menu, ChefBioFoodImage, MenuImage, Consumer, Date, Reserva



class ChefAdmin(admin.ModelAdmin):
	readonly_fields = ('image_tag',)
	fields = ['name', 'lastname', 'email', 'phone', 'picture', 'description', 'bio', 'comunas','image_tag']

admin.site.register(User)
admin.site.register(Chef, ChefAdmin)
admin.site.register(Comuna)
admin.site.register(Menu)
admin.site.register(ChefBioFoodImage)
admin.site.register(MenuImage)
admin.site.register(Consumer)
admin.site.register(Date)
admin.site.register(Reserva)