from django.db import models
from users.models import User, MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField("카테고리명", max_length=20)
    
    def __str__(self):
        return str(self.name)

class Post(models.Model):    
    title = models.CharField("제목", max_length=100)
    content = models.TextField("내용")
    image = models.ImageField("사진", blank=True, null=True, upload_to='%Y/%m/%d')
    star = models.IntegerField("별점", validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateField("생성일", auto_now_add=True)
    updated_at = models.DateField("마지막 수정일", auto_now=True)
    category = models.ForeignKey(Category, verbose_name="카테고리", on_delete=models.CASCADE)
    like = models.ManyToManyField(User, verbose_name="좋아요", related_name='like_posts')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment)
