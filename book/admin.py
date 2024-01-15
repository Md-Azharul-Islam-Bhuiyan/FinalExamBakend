from django.contrib import admin
from .models import BookModel, Comment, BookOverView


admin.site.register(BookModel)
admin.site.register(Comment)
admin.site.register(BookOverView)
