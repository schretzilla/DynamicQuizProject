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

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = (
            'id',
            'choice_text',
            'votes'
        )
#TODO: try adding a "choices" to the question model then serialize that cuz its a model serializer
class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = (
            'id',
            'question_text',
            'quiz',
            'date_created',
            'choices'
        )
