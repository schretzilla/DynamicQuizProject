from .models import Quiz

from rest_framework import serializers

class QuizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quiz
		fields = (
			'id',
			'quiz_name',
			'quiz_details',
			'question_set',
			'date_created'
			)