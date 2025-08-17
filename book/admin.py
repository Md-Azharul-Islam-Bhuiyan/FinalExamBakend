from django.contrib import admin
from .models import BookModel, Comment, LikePost, DisLikePost


admin.site.register(BookModel)
admin.site.register(Comment)
admin.site.register(LikePost)
admin.site.register(DisLikePost)
