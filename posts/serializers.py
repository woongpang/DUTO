from rest_framework import serializers

from posts.models import Post

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