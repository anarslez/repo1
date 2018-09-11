from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^user$', views.user),
    url(r'^result$', views.result),
    url(r'^session_word$', views.word),
    url(r'^sesh$', views.sesh),
]  