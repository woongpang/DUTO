from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator


class UserManager(BaseUserManager):
    def create_user(self, username, email, name, age, introduction, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
            age=age,
            introduction=introduction,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            email="admin2@admin.com",
            password=password,
            name="관리자2",
            age="7",
            introduction="관리자 계정입니다"
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField("유저 아이디", max_length=20, unique=True)
    email = models.EmailField("이메일", max_length=255, unique=True)
    name = models.CharField("이름", max_length=20)
    age = models.IntegerField(
        "나이", validators=[MinValueValidator(7), MaxValueValidator(220)])
    introduction = models.CharField("자기 소개", max_length=255, blank=True)
    
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin
