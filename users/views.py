from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from users.serializers import LoginViewSerializer, UserSerializer, UserProfileSerializer
from posts.serializers import PostSerializer
from users.models import User
from posts.models import Post
from django.contrib.auth import authenticate
from django.db.models.query_utils import Q

class UserView(APIView):
    def post(self, request):
        """회원가입"""
        username = request.data.get('username')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        name = request.data.get('name')
        email = request.data.get('email')
        age = request.data.get('age')
        introduction = request.data.get('introduction')

        if not (username and password1 and password2 and email):
            return Response({'error': '아이디, 비밀번호, 이메일은 필수값입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if password1 != password2:
            return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': '이미 사용 중인 아이디입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'error': '이미 사용 중인 이메일입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        User.objects.create_user(username=username, password=password1, name=name, email=email, age=age, introduction=introduction)

        return Response({'success': '회원가입이 완료되었습니다.'}, status=status.HTTP_201_CREATED)

class LoginView(TokenObtainPairView):
    """페이로드 커스터마이징"""
    serializer_class = LoginViewSerializer
    
    
class UserDeleteView(APIView):
    """회원탈퇴"""
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.is_active = False
        user.save()
        return Response("회원탈퇴가 완료되었습니다", status=status.HTTP_204_NO_CONTENT)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        """프로필 조회"""
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id):
        """프로필 수정"""
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowView(APIView):
    def post(self, request, user_id):
        """팔로잉 하기"""
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
