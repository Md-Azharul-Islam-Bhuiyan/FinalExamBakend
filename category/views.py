from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
