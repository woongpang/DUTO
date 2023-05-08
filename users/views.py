
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import LoginViewSerializer

class UserView(APIView):
    pass

class LoginView(TokenObtainPairView):
    """페이로드 커스터마이징"""
    serializer_class = LoginViewSerializer
class ProfileView(APIView):
    pass
class FollowView(APIView):
    pass
class MypostsView(APIView):
    pass
class LikesView(APIView):
    pass
