from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^/post$', views.post),
    url(r'^/comment$', views.comment),
]