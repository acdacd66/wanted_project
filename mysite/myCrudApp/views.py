# 데이터 처리
from .models import Board
from .serializers import BlogSerializer

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from django.http import Http404

from rest_framework.pagination import LimitOffsetPagination

# Blog의 목록을 보여주는 역할
class BlogList(APIView,LimitOffsetPagination):
    # Blog list를 보여줄 때
    def get(self, request):
        blogs = Board.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정

        page = self.paginate_queryset(blogs,request, view=self)
        if page is not None:
            serializer = BlogSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    # 새로운 Blog 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        board = Board()
        board.title = request.data['title']
        board.body = request.data['body']
        board.profile = request.user
        board.save() 
        
        return Response(status=status.HTTP_200_OK)

# Blog의 detail을 보여주는 역할
class BlogDetail(APIView):
    # Blog 객체 가져오기
    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Http404
    
    # Blog의 detail 보기
    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    # Blog 수정하기
    def put(self, request, pk, format=None):
        blog = self.get_object(pk)
        if blog.profile == request.user:#해당 유저의 글인 경우
            serializer = BlogSerializer(blog, data=request.data) 
        else:
            return Response("수정 권한이 없습니다.",status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Blog 삭제하기
    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        if blog.profile == request.user: #해당 유저의 글인 경우
            blog.delete()
        else:
            return Response("삭제 권한이 없습니다.",status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)      
    