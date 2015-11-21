from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Quiz, Question, Choice

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

    #confirm that all questions have been answered
    try:
        for question in quiz.question_set.all():
            if question.choice_set.all():
                request.POST['question'+ str(question.id)]
    except(KeyError, Choice.DoesNotExist):
        #redisplay the quiz if a question hasn't been answered
        return render(request, 'dynoquiz/quizdetail.html', {
            'quiz': quiz,
            'error_message': "You didn't answer all questions."
        })
    else:
        #add responses to database
        for question in quiz.question_set.all():
            if question.choice_set.all():
                selected_choice = question.choice_set.get(pk=request.POST['question'+ str(question.id)] )
                selected_choice.votes += 1
                selected_choice.save()

        return HttpResponseRedirect(reverse('dynoquiz:results', args=(quiz.id,)))

def results(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    context = {'quiz': quiz}
    return render(request, 'dynoquiz/results.html', context)

