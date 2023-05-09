from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase
from rest_framework import status
from posts.serializers import PostListSerializer
from users.models import User
from posts.models import Post

# Create your tests here.


class FollowingPostReadTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker()
        cls.posts = []
        for i in range(10):
            cls.user = User.objects.create_user(
                cls.faker.first_name(), cls.faker.word())
            cls.posts.append(Post.objects.create(category="study", title=cls.faker.sentence(
            ), content=cls.faker.text(), user=cls.user, star=5))

    def test_get_article(self):
        for article in self.articles:
            url = article.get_absolute_url()
            response = self.client.get(url)
            serializer = PostListSerializer(article).data
            for key, value in serializer.items():
                self.assertEqual(response.data[key], value)
                print(f"{key} : {value}")
