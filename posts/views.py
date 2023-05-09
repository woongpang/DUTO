from django.shortcuts import render
from rest_framework.views import APIView

class PostView(APIView):
    def get(self, request):
        """메인 페이지"""
        pass
    
class StudyFeedView(APIView):
    def get(self, request):
        """공부 게시판 글 목록 조회"""
        pass
    
class StudyFollowView(APIView):
    def get(self, request):
        """공부 게시판 팔로잉 게시글 목록 조회"""
        pass

class BreaktimeView(APIView):
    def get(self, request):
        """휴식 게시판 글 목록 조회"""
        pass
    
class BreaktimeFollowView(APIView):
    def get(self, request):
        """휴식 게시판 팔로잉 게시글 목록 조회"""
        pass
    
class PostDetailView(APIView):
    pass
class PostLikesView(APIView):
    pass
class CommentsView(APIView):
    pass
class CommentsDetailView(APIView):
    pass

