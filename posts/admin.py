from django.contrib import admin
from posts.models import Category, Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("category", "title", "created_at")


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
