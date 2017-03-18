from django.conf.urls import url

from . import views




app_name = 'words'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<word_id>[0-9]+)/classes/$', views.classes, name='classes'),
    url(r'^(?P<word_id>[0-9]+)/tasks/$', views.tasks, name='tasks'),
]
