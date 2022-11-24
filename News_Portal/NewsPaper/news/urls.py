from django.urls import path

from .views import (CategoriesList, AuthorsList, CommentsList, NewsList, ArticlesList, CategoryNewsList,
                    AuthorDetail, NewsDetail, CommentDetail, ArticleDetail,
                    NewsCreate, NewsUpdate, NewsDelete,
                    ArticleCreate, ArticleUpdate, ArticleDelete, subscribe, IndexView)

urlpatterns = [
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>', NewsDetail.as_view(), name='post_detail'),
    path('news/create/', NewsCreate.as_view()),
    path('news/<int:pk>/update/', NewsUpdate.as_view()),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),

    path('articles/', ArticlesList.as_view(), name='articles_list'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='post_detail'),
    path('articles/create/', ArticleCreate.as_view()),
    path('articles/<int:pk>/update/', ArticleUpdate.as_view()),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view()),

    path('categories/', CategoriesList.as_view()),
    path('categories/<int:pk>', CategoryNewsList.as_view()),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),

    path('authors/', AuthorsList.as_view()),
    path('authors/<int:pk>', AuthorDetail.as_view()),

    path('comments/', CommentsList.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),

    path('cunt/', IndexView.as_view())
]
