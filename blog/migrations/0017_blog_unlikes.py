# Generated by Django 4.1.3 on 2022-11-13 11:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0016_rename_like_blog_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='unlikes',
            field=models.ManyToManyField(related_name='userunlike', to=settings.AUTH_USER_MODEL),
        ),
    ]
