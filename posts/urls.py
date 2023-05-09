from django.urls import path
from posts import views

urlpatterns = [
    path('', views.PostView.as_view(), name='post_view'),
    path('study/', views.StudyFeedView.as_view(), name='study_feed_view'),
    path('study/followings/', views.StudyFollowView.as_view(), name='study_follow_view'),
    path('breaktime/', views.BreaktimeView.as_view(), name='breaktime_view'),
    path('breaktime/followings/', views.BreaktimeFollowView.as_view(), name='breaktime_follow_view'),
    path('<int:post_id>/', views.PostDetailView.as_view(), name='post_detail_view'),
    path('<int:post_id>/likes/', views.PostLikesView.as_view(), name='post_likes_view'),
    path('<int:post_id>/comments/', views.CommentsView.as_view(), name='comment_view'),
    path('<int:post_id>/comments/<int:comment_id>/', views.CommentsDetailView.as_view(), name='comments_detail_view'),
]