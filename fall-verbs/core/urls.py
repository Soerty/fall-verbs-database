from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

import index.views




urlpatterns = [
    url(r'^', include('index.urls')),
    url(r'^words/', include('words.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^prefs/', include('prefs.urls')),
    url(r'^classes/', include('classes.urls')),

]
