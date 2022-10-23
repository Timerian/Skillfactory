from django.urls import path
from .views import (PostsList, PostDetail, CategoriesList, CategoryDetail,
                    AuthorsList, AuthorDetail, CommentsList, CommentDetail)

urlpatterns = [
    path('news/', PostsList.as_view()),
    path('news/<int:pk>', PostDetail.as_view()),
    path('categories/', CategoriesList.as_view()),
    path('categories/<int:pk>', CategoryDetail.as_view()),
    path('authors/', AuthorsList.as_view()),
    path('authors/<int:pk>', AuthorDetail.as_view()),
    path('comments/', CommentsList.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),
]