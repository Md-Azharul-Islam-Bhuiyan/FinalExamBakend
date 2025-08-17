from django.db import models
from category.models import Category
from django.contrib.auth.models import User


class BookModel(models.Model):
    book_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="book/media/images/")
    category = models.ManyToManyField(Category, null=True, blank=True)
    posted_user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    like = models.IntegerField(default=0) 
    dislike = models.IntegerField(default=0)
    description = models.TextField()
    
    def __str__(self):
        return self.book_name
    

class Comment(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.book.book_name
    

class LikePost(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    like_post = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} Liked {self.book.book_name}"
    
    class Meta:
        verbose_name_plural = "LikePosts"
    
class DisLikePost(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    dislike_post = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} DisLiked {self.book.book_name}"
    
    class Meta:
        verbose_name_plural = "DisLikePosts"
    