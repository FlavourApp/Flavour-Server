from django.contrib import admin

# Register your models here.
from db.models import User, Chef, Comuna, Menu, ChefBioFoodImage, MenuImage, Consumer, Date

admin.site.register(User)
admin.site.register(Chef)
admin.site.register(Comuna)
admin.site.register(Menu)
admin.site.register(ChefBioFoodImage)
admin.site.register(MenuImage)
admin.site.register(Consumer)
admin.site.register(Date)