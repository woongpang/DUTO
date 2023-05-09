from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer, PostListSerializer, PostCreateSerializer

class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PostDetailView(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        # if request.user == post.user:
        serializer = PostCreateSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return Response("권한이 없습니다.", status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        # if request.user == post.user:
        #     post.delete()
        #     return Response("삭제되었습니다", status=status.HTTP_204_NO_CONTENT)
        # else:
        #     return Response("권한이 없습니다.", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
class PostLikesView(APIView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            return Response("unfollow", status=status.HTTP_200_OK)
        else:
            post.likes.add(request.user)
            return Response("follow", status=status.HTTP_200_OK)    
        
        
class StudyFeedView(APIView):
    pass
class StudyFollowView(APIView):
    pass
class BreaktimeView(APIView):
    pass
class BreaktimeFollowView(APIView):
    pass
class CommentsView(APIView):
    pass
class CommentsDetailView(APIView):
    pass

