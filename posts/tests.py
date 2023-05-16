from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase
from rest_framework import status
from posts.serializers import PostListSerializer
from users.models import User
from posts.models import Post

# Create your tests here.
