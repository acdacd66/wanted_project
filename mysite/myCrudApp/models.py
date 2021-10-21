from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pubdate=models.DateField(auto_now_add=True,verbose_name='날짜',null=True)
    profile= models.ForeignKey(
        User,
        on_delete=models.CASCADE,null=True
    )


