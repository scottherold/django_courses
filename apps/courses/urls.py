from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/$', views.index),
    url(r'^courses/create/$', views.create),
    url(r'^courses/destroy/(?P<number>\d+)/$', views.destroy),
]