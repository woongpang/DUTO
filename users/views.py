from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from users.serializers import LoginViewSerializer, UserSerializer
from posts.serializers import PostSerializer
from users.models import User
from posts.models import Post
from django.contrib.auth import authenticate
from django.db.models.query_utils import Q

class UserView(APIView):
    pass

class LoginView(TokenObtainPairView):
    """페이로드 커스터마이징"""
    serializer_class = LoginViewSerializer
    
    def post(self, request):
        try:
            username = request.data.get("username", "")
            password = request.data.get("password", "")
            
            user = authenticate(request, username=username, password=password)
            
            user_serializer = UserSerializer(user)
            token = LoginViewSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            
            response = Response(
                {
                    "message" : "로그인 성공",
                    "id" : user_serializer.data["id"],
                    "username" : user_serializer.data["username"],
                    "email" : user_serializer.data["email"],
                    "follower" : user_serializer.data["followings"],
                    "token" : {
                        "refresh" : refresh_token,
                        "access" : access_token,
                    }
                }
            )
            
            return response
        except AttributeError:
            return Response("username 또는 password가 다릅니다.", status=status.HTTP_403_FORBIDDEN)
    
class ProfileView(APIView):
    pass

class FollowView(APIView):
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        me = request.user
        
        if me in you.followers.all():
            you.followers.remove(me)
            return Response("unfollow했습니다.",status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            return Response("follow했습니다.",status=status.HTTP_200_OK)
        

class MypostsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        post = Post.objects.filter(user=request.user)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
        # q = Q()
        # for user in request.user.posts.all():
        #     q.add(Q(user=user), q.OR)
        # posts = Post.objects.filter(q)
        # serializer = PostSerializer(posts, many=True)
        # return Response(serializer.data)
    
class LikesView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        post = Post.objects.filter(like=request.user)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
