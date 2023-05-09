from django.urls import path
from posts import views

urlpatterns = [
    path('', views.PostView.as_view(), name='post_view'),
    path('<str:category_name>/',
         views.CategoryView.as_view(), name='category_view'),
    path('<str:category_name>/followings/', views.CategoryFollowView.as_view(),
         name='category_follow_view'),
    path('<int:post_id>/', views.PostDetailView.as_view(), name='post_detail_view'),
    path('<int:post_id>/likes/', views.PostLikesView.as_view(), name='post_likes_view'),
    path('<int:post_id>/comments/', views.CommentsView.as_view(), name='comment_view'),
    path('<int:post_id>/comments/<int:comment_id>/', views.CommentsDetailView.as_view(), name='comments_detail_view'),
]