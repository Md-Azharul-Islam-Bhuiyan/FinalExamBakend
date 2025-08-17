from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import BookModel, Comment, LikePost, DisLikePost
from .serializers import BookSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import pagination, filters
from rest_framework.authentication import  BasicAuthentication, TokenAuthentication


class BookPaginatination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = page_size
    max_page_size = 100

class SpecificBook(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        book_id = request.query_params.get("book_id")
        if book_id:
            return query_set.filter(book=book_id)
        return query_set

class BookViewSet(viewsets.ModelViewSet):
    queryset=BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    pagination_class = BookPaginatination
    filter_backends = [filters.SearchFilter]
    search_fields = ['book_name']
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
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Set the author before saving
        serializer.validated_data['user'] = request.user
        # BookOverView.objects.create(book=serializer)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)







def LikePostView(request, id):
    book_obj = get_object_or_404(BookModel, id=id)
    
    if LikePost.objects.filter(post=book_obj, user=request.user).exists():
        print('You have already liked this post.')
        # return redirect('home')
    else:
        
        book_obj.like += 1
        book_obj.save()
        
        LikePost.objects.create(post=book_obj, user=request.user, like_post=1)
    return redirect('home')

def DisLikePostView(request, id):
    book_obj = get_object_or_404(BookModel, id=id)
    
    if DisLikePost.objects.filter(post=book_obj, user=request.user).exists():
            print('You have already liked this post.')
    else:
        
        book_obj.like += 1
        book_obj.save()
        
        DisLikePost.objects.create(post=book_obj, user=request.user, dislike_post=1)
    return redirect('home')    