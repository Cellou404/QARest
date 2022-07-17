from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework import generics
from .models import *
from .serializers import *

from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor

# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slug'

    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


# Answer Create Generic View
class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=slug)
        serializer.save(author=user, question=question)


# Answer list Generic View
class AnswerList(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug=slug)


# Answer Update - Delete
class AnswerDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
