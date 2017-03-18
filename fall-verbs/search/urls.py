from django.conf.urls import url

from . import views

app_name = 'search'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^components/$', views.filter_components, name='components'),
    url(r'^_query/$', views.query, name='query'),
]