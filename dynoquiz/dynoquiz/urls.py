from django.conf.urls import url

from . import views

urlpatterns = [
    #Home Page
    url(r'^quiz/$', views.index, name='index'),
    #Quiz Question Details
    url(r'^(?P<quiz_id>[0-9]+)/$', views.detail, name='quiz_detail')
]