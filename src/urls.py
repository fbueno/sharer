from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^sharer/', include('sharer.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^confirm/(?P<key>.*)', 'people.views.confirm'),
    (r'^register', 'people.views.register'),
    (r'^login/', include('login.urls')),
    (r'^upload', 'f.views.upload'),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
    (r'^(?P<key>.*)', 'f.views.download'),
)
