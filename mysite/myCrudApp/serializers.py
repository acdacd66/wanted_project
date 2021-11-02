from .models import Board,Comment,Nested_Comment
from rest_framework import serializers

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class NestedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nested_Comment
        fields = '__all__'

