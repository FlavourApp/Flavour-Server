from django.conf.urls import url

from flavourdb2 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chefs/$', views.chefs, name='chefs'),
    url(r'^mainView/$', views.mainView, name='mainView'),
    url(r'^addConsumer/$', views.addConsumer, name='addConsumer'),
    url(r'^dates/$', views.dates, name='dates'),

]