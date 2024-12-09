from rest_framework import serializers
from rest_framework.reverse import reverse

from Base.models import Article
from .views import *

class ArticleSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='Api:ArticleDetailApiView', lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Article
        fields = [
            'url',
            'edit_url',
            'pk',
            'owner',
            'category',
            'title',
            'body',
            'created',
            'updated'
        ]

    def get_edit_url(self, obj):
        request = self.context.get('request')
        return reverse('Api:ArticleUpdateApiView', kwargs={'pk':obj.pk}, request=request)