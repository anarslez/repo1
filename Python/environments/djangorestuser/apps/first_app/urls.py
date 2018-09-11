from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new), 
    url(r'^add$', views.add),
    url(r'^(?P<id>\d)$', views.show, name = 'show'), 
    url(r'^(?P<id>\d+)/edit$', views.edit, name = 'edit'),
    url(r'^edit$', views.edituser),
    url(r'^update$', views.update),
    url(r'^show$', views.showuser),  
]    