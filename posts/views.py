from django.db.models.query_utils import Q
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from posts.models import Post
from posts.serializers import PostListSerializer

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
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, category_name):
        """카테고리별 팔로잉 게시글 목록 조회"""
        q = Q()
        for user in request.user.followings.all():
            q.add(Q(user=user), q.OR)
        following_posts = Post.objects.filter(q, category__name=category_name)
        print(q)
        serializer = PostListSerializer(following_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class PostDetailView(APIView):
    pass
class PostLikesView(APIView):
    pass
class CommentsView(APIView):
    pass
class CommentsDetailView(APIView):
    pass

