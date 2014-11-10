from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from db import views
from db import data_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^data/chefs/$', data_views.chefs, name='chefs'),
    url(r'^data/dates/$', data_views.dates, name='dates'),
    url(r'^reserva/$', views.reserva, name='reserva'),




]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
