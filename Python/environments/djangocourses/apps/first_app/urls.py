from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^(?P<id>\d)/delete$', views.delete, name = 'delete'),
    url(r'^delete$', views.deletewarning),
    url(r'^confirm$', views.confirm),
]  