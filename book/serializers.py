from rest_framework import serializers
from .models import BookModel, Comment, BookOverView


class BookSerializer(serializers.ModelSerializer):
     class Meta:
          model = BookModel
          exclude = ['posted_user']


class CommentSerializer(serializers.ModelSerializer):
     class Meta:
          model = Comment
          fields = '__all__'


class BookOverViewSerializer(serializers.ModelSerializer):
     class Meta:
          model = BookOverView
          fields = '__all__'
