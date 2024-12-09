from django.urls import path
from .views import *

app_name = 'Base'

urlpatterns = [
    path('', home, name='home'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('register/', registerView, name='register'),
    path('user-detail/', userDetailView, name='user-detail'),
    path('update-user/', updateUserView, name='update_user'),
    path('delete-user/', deleteUserView, name='delete_user'),
    path('article-create/', articleCreateView, name='article_create'),
    path('article-detail/<int:pk>', articleDetailView, name='article_detail'),
    path('article-update/<int:pk>', articleUpdateView, name='article_update'),
    path('article-delete/<int:pk>', articleDeleteView, name='article_delete'),
]
