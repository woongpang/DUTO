from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    followings = serializers.StringRelatedField(many=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = "__all__"
    
    # 회원가입시 비밀번호를 해싱(암호화) 하는 함수
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def validate_email(self, email):
        try:
            validate_email(email)
            return email
        except ValidationError:
            raise serializers.ValidationError('유효하지 않은 이메일 형식입니다.')


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

class UserProfileSerializer(serializers.ModelSerializer):
    followings = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'age', 'introduction', 'followings']