from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>\d)$', views.show),
    url(r'^create$', views.create),
    url(r'^add$', views.add),
    url(r'^delete$', views.delete)
]