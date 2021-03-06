from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),

    url(r'^addItem/$', views.addItem, name = 'addItem'),
    url(r'^deleteItem/(?P<id>.+)$', views.deleteItem, name = 'deleteItem'),
    url(r'^addlist/(?P<id>.+)$', views.addToList, name = 'addToList'),
    url(r'^removelist/(?P<id>.+)$', views.removeFromList, name = 'removeFromList'),
    url(r'^item/(?P<id>.+)$', views.item, name = 'item'),
    url(r'^create/$', views.create, name = 'create'),
]