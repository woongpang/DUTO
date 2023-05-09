
from django.db.models.query_utils import Q
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from posts.serializers import PostSerializer, PostListSerializer, PostCreateSerializer
from posts.models import Post


class PostView(APIView):
    def get(self, request):
        """메인 페이지"""
        """
        공부 카테고리에서 글 상위 10개(24시간 조회수 기준),
        휴식 카테고리에서 글 상위 10개(24시간 조회수 기준),
        공부 카테고리에서 글 상위 3개(좋아요 기준),
        휴식 카테고리에서 글 상위 3개(좋아요 기준),
        """

        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CategoryView(APIView):
    def get(self, request, category_name):
        """카테고리별 글 목록 조회"""
        posts = Post.objects.filter(category__name=category_name)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryFollowView(APIView):
    def get(self, request, category_name):
        """카테고리별 팔로잉 게시글 목록 조회"""
        pass

class PostView(APIView):
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
        
        # if request.user == post.user:
        #     post.user.is_active(False)
        
    # request.user.is_active = False
    # request.user.save()
        
class PostLikesView(APIView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            return Response("unfollow", status=status.HTTP_200_OK)
        else:
            post.likes.add(request.user)
            return Response("follow", status=status.HTTP_200_OK)    


