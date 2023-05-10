from django.db.models.query_utils import Q
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from posts.models import Post, Comment
from posts.serializers import PostSerializer, PostListSerializer, PostCreateSerializer, CommentSerializer, CommentCreateSerializer

class PostView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"message":"로그인 해주세요"}, 401)
        
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
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
        if request.user in post.like.all():
            post.like.remove(request.user)
            return Response("좋아요 취소", status=status.HTTP_200_OK)
        else:
            post.like.add(request.user)
            return Response("좋아요", status=status.HTTP_200_OK)
        
        
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
        
        
class CommentsView(APIView):
    def get(self, request, post_id):
        posts = Post.objects.get(id=post_id)
        comments = posts.comment_set.all() # Post를 참조하는 comment들의 집합(comment_set) 모두(.all)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, post_id):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post_id=post_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CommentsDetailView(APIView):
    def put(self, request, post_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:        
            serializer = CommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('권한이 없습니다!', status=status.HTTP_403_FORBIDDEN)    

    def delete(self, request, post_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            comment.delete()
            return Response('삭제되었습니다!', status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('권한이 없습니다!', status=status.HTTP_403_FORBIDDEN)