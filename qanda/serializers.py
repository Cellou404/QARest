from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Answer
        exclude = ['question']