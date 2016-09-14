from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from db import views
from db import data_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^data/chefs/$', data_views.chefs, name='data_chefs'),
    url(r'^data/dates/$', data_views.dates, name='data_dates'),
    url(r'^data/menus/$', data_views.menus, name='data_menus'),
    url(r'^data/comunas/$', data_views.comunas, name='data_comunas'),
    url(r'^(?P<chefid>[0-9]+)/menus/$', views.menus, name='menus'),
    url(r'^createPayment/$', views.pay_khipu, name='pay_khipu'),
    url(r'^successfulPayment/$', views.sucsessful_payment, name='sucsessful_payment'),
    url(r'^emailtest/$', views.emailtest, name='emailtest'),

]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
