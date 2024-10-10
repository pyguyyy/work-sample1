from django.urls import path
from .views import *

app_name = 'Base'

urlpatterns = [
    path('', home, name='home'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='login'),
    path('register/', registerPage, name='register'),
    path('update-user/', updateUserPage, name='update_user'),
    path('delete-user/', deleteUserPage, name='delete_user'),
    path('article-create/', articleCreatePage, name='article_create'),
    path('article-detail/<int:pk>', articleDetailPage, name='article_detail'),
    path('article-update/<int:pk>', articleUpdatePage, name='article_update'),
    path('article-delete/<int:pk>', articleDeletePage, name='article_delete'),

]
