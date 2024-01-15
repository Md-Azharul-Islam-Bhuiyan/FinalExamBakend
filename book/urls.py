from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('list', views.BookViewSet)
router.register('comment/list', views.CommentViewSet)
router.register('postoverview/list', views.BookOverViewViewset)


urlpatterns = [
    path('', include(router.urls))
]



