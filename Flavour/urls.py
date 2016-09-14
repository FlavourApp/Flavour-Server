from django.conf.urls import *
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Flavour.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('db.urls'))

]
