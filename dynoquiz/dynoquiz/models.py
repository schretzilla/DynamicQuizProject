from django.db import models

#A quiz contains many questions
class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100)
    date_created = models.DateTimeField('date created')
    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    question_text = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created')
    def __str__(self):
        return self.question_text
