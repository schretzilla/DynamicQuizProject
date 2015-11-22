from django.conf.urls import url

from . import views

urlpatterns = [
    #Home Page
    #url(arg1 = just for visual url, ar2=method to use, arg3= alias to ref this )
    url(r'^quiz/$', views.index, name='index'),
    #Quiz Question Details
    url(r'^quiz/(?P<quiz_id>[0-9]+)/$', views.quizdetail, name='quiz_detail'),
    #Vote on Quiz
    url(r'^quiz/(?P<quiz_id>[0-9]+)/vote/$', views.vote, name ='vote'),
    #Results of Quiz
    url(r'^quiz/(?P<quiz_id>[0-9]+)/results/$', views.results, name='results'),
    #New Quiz Form
    url(r'^quiz/newquiz/$', views.newquiz, name='new_quiz'),
    #Create New Quiz
    url(r'^quiz/createquiz/$', views.createquiz, name='create_quiz'),
    #New Question
    url(r'^quiz/(?P<quiz_id>[0-9]+)/newquestion/$', views.newquestion, name='new_question'),
    #Add New Question
    url(r'^quiz/(?P<quiz_id>[0-9]+)/addquestion/$', views.addquestion, name='create_question')
]