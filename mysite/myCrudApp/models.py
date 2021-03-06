from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# from djongo import models
User = get_user_model()

class Board(models.Model):
    title = models.CharField(max_length=100,null=True)
    content = models.TextField(null=True)
    pubdate=models.DateField(auto_now_add=True,verbose_name='날짜',null=True)
    author= models.ForeignKey(
        User,
        on_delete=models.CASCADE,null=True
    )
    view_user = models.ManyToManyField(User,blank=True,related_name='user_view')
    view_count = models.IntegerField(default = 0,null = True)
    catagory = models.IntegerField(null = True)


class Comment(models.Model):
    content = models.TextField(null=True)
    author= models.ForeignKey(
        User,
        on_delete=models.CASCADE,null=True
    )
    board_id= models.ForeignKey(
        Board,
        on_delete=models.CASCADE,null=True
    )

class Nested_Comment(models.Model):
    content = models.TextField(null=True)
    author= models.ForeignKey(
        User,
        on_delete=models.CASCADE,null=True
    )
    comment_id= models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,null=True
    )