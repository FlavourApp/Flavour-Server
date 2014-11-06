from django.contrib import admin

# Register your models here.
from flavourdb2.models import User, Chef, Comuna, Menu, ChefBioFoodImage, MenuImage, Consumer


admin.site.register(User)
admin.site.register(Chef)
admin.site.register(Comuna)
admin.site.register(Menu)
admin.site.register(ChefBioFoodImage)
admin.site.register(MenuImage)
admin.site.register(Consumer)