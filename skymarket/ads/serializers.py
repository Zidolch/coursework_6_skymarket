from rest_framework import serializers
from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField(source='id')
    author_id = serializers.ReadOnlyField(source='author.id')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    author_image = serializers.ImageField(source='author.image', read_only=True)
    ad_id = serializers.ReadOnlyField(source='ad.id')

    class Meta:
        model = Comment
        exclude = ['id', 'author', 'ad']


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description']


class AdDetailSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField(source='id')
    author_id = serializers.ReadOnlyField(source='author.id')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    phone = serializers.ReadOnlyField(source='author.phone')

    class Meta:
        model = Ad
        exclude = ['id', 'author', 'created_at']

