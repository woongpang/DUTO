from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class LoginViewSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['name'] = user.name
        token['age'] = user.age

        return token
