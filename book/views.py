from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import BookModel, Comment, BookOverView
from .serializers import BookSerializer, CommentSerializer, BookOverViewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BookViewSet(viewsets.ModelViewSet):
    queryset=BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Set the author before saving
        serializer.validated_data['posted_user'] = request.user
        # BookOverView.objects.create(book=serializer)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    # def perform_create(self, serializer):
    #     book_instance = serializer.save(posted_user=self.request.user)

    #     # Create corresponding BookOverView instance
        # BookOverView.objects.create(book=book_instance)

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

   



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer


class BookOverViewViewset(viewsets.ModelViewSet):
    queryset = BookOverView.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BookOverViewSerializer
