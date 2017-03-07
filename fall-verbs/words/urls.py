from django.conf.urls import url
from django.conf.urls import include

from . import views




app_name = 'words'
urlpatterns = [
    url(r'$', views.index, name='index'),
    url(r'(?P<word_id>[0-9]+)/', include([
        url(r'sense/$', views.sense, name='sense'),
    ])),
]
