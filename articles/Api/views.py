from django.shortcuts import render

from rest_framework import generics

from Base.models import Article
from .serializers import ArticleSerializer
from .mixins import StaffEditorPermissionMixin

# Create your views here.
class ArticleListCreateApiView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        body = serializer.validated_data.get('body') or None
        if body is None:
            body = title
        serializer.save(body=body)

class ArticleDetailApiView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field='pk'

class ArticleUpdateApiView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'


    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.body:
            instance.body = instance.name


class ArticleDestroyApiView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'


    def perform_destroy(self, instance):
        super().perform_destroy(instance)