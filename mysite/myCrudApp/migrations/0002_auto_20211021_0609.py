# Generated by Django 3.2.8 on 2021-10-20 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myCrudApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='pubdate',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='날짜'),
        ),
    ]