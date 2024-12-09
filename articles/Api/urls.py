from django.urls import path

from .views import *

app_name = 'Api'

urlpatterns = [
    path('articles/', ArticleListCreateApiView.as_view(), name='ArticleListCreateApiView'),
    path('articles/<int:pk>/', ArticleDetailApiView.as_view(), name='ArticleDetailApiView'),
    path('articles/<int:pk>/update/', ArticleUpdateApiView.as_view(), name='ArticleUpdateApiView'),
    path('articles/<int:pk>/delete/', ArticleDestroyApiView.as_view(), name='ArticleDestroyApiView'),
]


