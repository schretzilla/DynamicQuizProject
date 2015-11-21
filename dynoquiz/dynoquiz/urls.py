from django.conf.urls import url

from . import views

urlpatterns = [
    #Home Page
    url(r'^quiz/$', views.index, name='index'),
    #Quiz Question Details
    url(r'^quiz/(?P<quiz_id>[0-9]+)/$', views.quizdetail, name='quiz_detail'),
    #Vote on Quiz
    url(r'^quiz/(?P<quiz_id>[0-9]+)/vote/$', views.vote, name ='vote'),
]