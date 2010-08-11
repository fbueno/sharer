from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^(?P<orig_url>.*)', 'login.views.sitelogin'),
)
