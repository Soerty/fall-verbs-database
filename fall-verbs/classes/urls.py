from django.conf.urls import url

from . import views




app_name = 'classes'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<class_id>[0-9]+)/wordlist/$', views.wordlist, name='wordlist'),
]
