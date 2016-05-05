from .models import Quiz, Question, Choice

from rest_framework import serializers

class QuizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quiz
		fields = (
			'id',
			'quiz_name',
			'quiz_details',
			'date_created'
			)

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'question_text',
            'quiz',
            'date_created'
        )

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = (
            'id',
            'choice_text',
            'votes'
        )
