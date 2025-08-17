from rest_framework import serializers
from .models import BookModel, Comment


class BookSerializer(serializers.ModelSerializer):
     class Meta:
          model = BookModel
          exclude = ['posted_user']


class CommentSerializer(serializers.ModelSerializer):
     class Meta:
          model = Comment
          exclude = ['user']


