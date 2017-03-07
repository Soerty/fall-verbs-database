from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

import index.views




urlpatterns = [
    url(r'^$', index.views.index),
    url(r'^words/', include('words.urls')),
    url(r'^admin/', admin.site.urls),
]
