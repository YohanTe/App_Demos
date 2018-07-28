from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^newpost$', views.newpost),
    url(r'^delete/(?P<number>\d+)$', views.delete)
]