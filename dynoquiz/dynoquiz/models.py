from django.db import models

#A quiz contains many questions
class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100)
    quiz_details = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField('date created')
    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    question_text = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
