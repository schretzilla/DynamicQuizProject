from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Quiz, Question

def index(request):
    quiz_list = Quiz.objects.all()
    context = {'quiz_list': quiz_list}
    return render(request, 'dynoquiz/index.html', context)

def quizdetail(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    context = {'quiz': quiz}
    return render(request, 'dynoquiz/quizdetail.html', context)

def vote(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    for question in quiz.question_set.all():
        #confirm that there are choices for the question
        if question.choice_set.all():
            selected_choice = question.choice_set.get(pk=request.POST['question'+ str(question.id)] )
            if selected_choice:
                selected_choice.votes += 1
                selected_choice.save()

    return HttpResponseRedirect(reverse('dynoquiz:index'))

