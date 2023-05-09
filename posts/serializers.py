from rest_framework import serializers
from posts.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    
    # def get_user(self, obj):
    #     return obj.user.username
    
    class Meta:
        model = Post
        fields = '__all__'
        
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "image", "content")
        
class PostListSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    
    # def get_user(self, obj):
    #     return obj.user.username
    
    class Meta:
        model = Post
        fields=("title", "content", "created_at")

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Comment
        exclude = ('post',)

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment',)
