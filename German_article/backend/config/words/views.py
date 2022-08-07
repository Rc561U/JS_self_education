from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from .import models
import random
from rest_framework.response import Response
from django.http import HttpResponseNotFound


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Words
        fields = ['pk','gender','word']


class RandomWowrd(APIView):
    def get(self,*args, **kwargs):
        all_words = models.Words.objects.all()
        random_word = random.choice(all_words)
        serialized_random_word = WordSerializer(random_word, many=False)
        return Response(serialized_random_word.data)

class NextWord(APIView):
    def get(self, request, pk, format=None):
        word = models.Words.objects.filter(pk__gt=pk).first()
        if not word:
            return HttpResponseNotFound('fuck you')
        serialized_word = WordSerializer(word, many=False)
        return Response(serialized_word.data)
