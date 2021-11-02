# 데이터 처리
from .models import Board,Comment,Nested_Comment
from .serializers import BoardSerializer,CommentSerializer,NestedCommentSerializer

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
            serializer = BoardSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = BoardSerializer(blogs, many=True)
        return Response(serializer.data)

    # 새로운 Blog 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        board = Board()
        board.title = request.data['title']
        board.content = request.data['content']
        board.catagory = request.data['catagory']
        board.author = request.user
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
        board = self.get_object(pk)
        board.view_user.add(request.user)
        board.view_count = board.view_user.count()
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    # Blog 수정하기
    def put(self, request, pk, format=None):
        board = self.get_object(pk)
        if board.author == request.user:#해당 유저의 글인 경우
            serializer = BoardSerializer(board, data=request.data) 
        else:
            return Response("수정 권한이 없습니다.",status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Blog 삭제하기
    def delete(self, request, pk, format=None):
        board = self.get_object(pk)
        if board.author == request.user: #해당 유저의 글인 경우
            board.delete()
        else:
            return Response("삭제 권한이 없습니다.",status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)      
    


class CommentCrud(APIView,LimitOffsetPagination):
    def get(self, request):
        board_pk = request.query_params.get('board_id', '') 
        comments = Comment.objects.filter(board_id = board_pk)
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정

        page = self.paginate_queryset(comments,request, view=self)
        if page is not None:
            serializer = CommentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    # 새로운 Blog 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        comment = Comment()
        
        comment.content = request.data['content']
        comment.author = request.user
        comment.board_id = Board.objects.get(pk = request.data['board_id'])
        comment.save() 
        
        return Response(status=status.HTTP_200_OK)

class NestedCommentCrud(APIView,LimitOffsetPagination):
    def get(self, request):
        comment_pk = request.query_params.get('comment_id', '') 
        comments = Nested_Comment.objects.filter(comment_id = comment_pk)
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정

        page = self.paginate_queryset(comments,request, view=self)
        if page is not None:
            serializer = NestedCommentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = NestedCommentSerializer(comments, many=True)
        return Response(serializer.data)
    # 새로운 Blog 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        comment = Nested_Comment()
        
        comment.content = request.data['content']
        comment.author = request.user
        comment.comment_id = Comment.objects.get(pk = request.data['comment_id'])
        comment.save() 
        
        return Response(status=status.HTTP_200_OK)