from rest_framework import serializers
from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Comment
        exclude = ('post',)


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment',)


class MainPostSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.category.name

    def get_like_count(self, obj):
        return obj.like.count()

    def get_comments_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Post
        fields = ("category", "title", "comments_count",
                  "like_count", "created_at")


class PostListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.category.name

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Post
        fields = ("pk", "category", "user", "title", "content",
                  "image", "star", "like_count", "updated_at",)


class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("category", "title", "image", "content", "star")
