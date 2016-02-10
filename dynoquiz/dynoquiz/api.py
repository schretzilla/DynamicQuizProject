from .models import Quiz
from .serializers import QuizSerializer
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

class QuizList(APIView):
	def get(self, request, fromat=None):
		quizes = Quiz.objects.all()
		serialized_quiz = QuizSerializer(quizes, many=True)
		return Response(serialized_quiz.data)

	def post(self, request, format=None):
		serializer = QuizSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuizDetail(APIView):
    def get_quiz(self, pk):
        try:
            return Quiz.objects.get(pk=pk)
        except Quiz.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        quiz = self.get_quiz(pk)
        serialized_quiz = QuizSerializer(quiz)
        return Response(serialized_quiz.data)

    def delete(self, request, pk, format=None):
        quiz = self.get_quiz(pk)
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, format=None):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            quiz = self.get_quiz(serializer.id)

            #make update function in model class
            quiz.quiz_name = serializer.quiz_name
            quiz.quiz_details = serializer.quiz_details
            quiz.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)